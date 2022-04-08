from django.shortcuts import render
from django.http import HttpResponse
from rest_framework import viewsets
from .serializers import *
from .models import *
from django.views.generic import TemplateView, DetailView
from rest_framework.response import Response
from rest_framework_tracking.mixins import LoggingMixin
from django.http import JsonResponse
import json, datetime, math
import pandas as pd
from dateutil.relativedelta import relativedelta
from django.db.models import Count,Sum
from django.db.models.functions import Extract
from django.db.models import F, Value
from django.db.models.functions import Concat
from django.db import connection



# Create your views here.

class AugmentEntryViewAPI(LoggingMixin, viewsets.ViewSet):
    def list(self, request):
        queryset = AugmentEntryView.objects.all()
        serializer = AugmentEntryViewSerializer(queryset, many=True)
        data = {
            'requests': serializer.data
        }

        return Response(data)



class AugmentEntriesAPI(LoggingMixin, viewsets.ViewSet):
    def list(self, request):
        queryset = AugmentEntries.objects.all()
        serializer = AugmentEntriesSerializer(queryset, many=True)
        return Response(serializer.data)

class CurrentCapacityAPI(LoggingMixin, viewsets.ViewSet):
    def list(self, request):
        queryset = CurrentCapacity.objects.all()
        serializer =CurrentCapacitySerializer(queryset, many=True)
        return Response(serializer.data)

class DashboardViewAPI(LoggingMixin, viewsets.ViewSet):
    def list(self, request):
        queryset = DashboardView.objects.all()
        serializer = DashboardViewSerializer(queryset, many=True)
        data = {
            'requests': serializer.data
        }

        return Response(data)

    def datetime_handler(x):
        if isinstance(x, datetime.datetime):
            return x.isoformat()
        raise TypeError("Unknown type")

    def retrieve(self, request,pk=None):
        
        print(pk, 'Received Per User Action on Homepage!')
        print('Retrieved QuerySet:', DashboardView.objects.filter(id=pk).values())
        
        dictPk = DashboardView.objects.filter(id=pk).values()[0]
        gr = 0.2325
        threshold = 0.7

        pathName = str(dictPk['path_name'] if 'path_name' in dictPk else 0)
        reportingDate = datetime.datetime.strptime(str(dictPk['reporting_date'] if 'reporting_date' in dictPk else 0),'%Y-%m-%d').date()
        currentCapacity = float(dictPk['capacity_gbps'] if 'capacity_gbps' in dictPk else 0)
        wcfTraffic = float(dictPk['wcf_traffic_gbps'] if 'wcf_traffic_gbps' in dictPk else 0)

        endStateCapacity = int(round(((wcfTraffic * ((1+gr)**(15/12)))/threshold / 100.0),0)) * 100
        endStateCapacity = endStateCapacity if endStateCapacity > currentCapacity else currentCapacity

        responses = list(DashboardView.objects.filter(path_name=pathName,
                                                reporting_date__lte=reportingDate).values('path_name', 'reporting_date',
                                                                                            'capacity_gbps', 'wcf_traffic_gbps'))
                
        for response in responses:
            response['wcf_projected_util'] = 0
            response['capacity_gbps'] = float(response['capacity_gbps'])
            response['end_state_capacity_gbps'] = endStateCapacity
            response['wcf_util'] = 0 if 'capacity_gbps' not in response else float(response['wcf_traffic_gbps'])/float(response['capacity_gbps']) if 'wcf_traffic_gbps' in response else 0
            response['wcf_util_es'] = float(response['wcf_traffic_gbps'])/endStateCapacity if 'wcf_traffic_gbps' in response else 0
            response['wcf_projected_util_es'] = 0
            response['reporting_date'] = response['reporting_date'].isoformat()
            del response['wcf_traffic_gbps']
        
        responses[-1]['wcf_projected_util'] = responses[-1]['wcf_util']
            
        reportingDate += relativedelta(months=1)

        r = 15
        while r>0:            
            
            wcfTraffic *= ((1+gr)**(1/12))
            responses.append({
                'path_name':pathName,
                'reporting_date':reportingDate.isoformat(),
                'capacity_gbps':currentCapacity,
                'wcf_projected_util':wcfTraffic/currentCapacity,
                'end_state_capacity_gbps':endStateCapacity,
                'wcf_util':0,
                'wcf_util_es':0,
                'wcf_projected_util_es':wcfTraffic/endStateCapacity
            })

            reportingDate += relativedelta(months=1)
            r-=1
                 
        responses = json.dumps(responses)
        responses = json.loads(responses)

        return JsonResponse(responses, safe=False)
        



class LocationAPI(LoggingMixin, viewsets.ViewSet):
    def list(self, request):
        queryset = Location.objects.all()
        serializer = LocationSerializer(queryset, many=True)
        return Response(serializer.data)

class NodeAPI(LoggingMixin, viewsets.ViewSet):
    def list(self, request):
        queryset = Node.objects.all()
        serializer = NodeSerializer(queryset, many=True)
        return Response(serializer.data)

class PathAPI(LoggingMixin, viewsets.ViewSet):
    def list(self, request):
        queryset = Path.objects.all()
        serializer = PathSerializer(queryset, many=True)
        return Response(serializer.data)

class TrafficInfoAPI(LoggingMixin, viewsets.ViewSet):
    def list(self, request):
        queryset = TrafficInfo.objects.all()
        serializer = TrafficInfoSerializer(queryset, many=True)
        return Response(serializer.data)

class DisplayTrafficInfo(TemplateView):
    model = TrafficInfo
    template_name = 'TrafficInfo.html'

    def get_queryset(self):
        return TrafficInfo.objects.all()

# ---Frontend hooks---- api for the  dashboardView

sql_myfilter = """SELECT a.reporting_date, a.legacy_company, a.a_location, a.z_location, a.a_node,
 a.z_node, a.path_name, a.segment_type, a.leased,
a.current_capacity_gbps, a.capacity_gbps, a.ssp_traffic_gbps,
 a.wcf_traffic_gbps, a.current_ssp_util, a.current_wcf_util, a.id, MONTHNAME(a.reporting_date) AS path_month,
 YEAR(a.reporting_date) AS path_year, b.path_info_id FROM dashboard_view a
LEFT JOIN path_info b ON a.path_name = b.path_info_name;"""

sql_pathinfo = """ SELECT a.path_name,a.current_wcf_util, b.path_info_id,ROUND(((ROUND(CONVERT(((a.wcf_traffic_gbps*(POWER(1.2325,1.25)))/0.75), UNSIGNED),-2))/a.current_capacity_gbps),0) AS end_state,
CONCAT(SUBSTRING(MONTHNAME(a.reporting_date),1,3),'-', YEAR(a.reporting_date)) AS path_date
 FROM dashboard_view a
LEFT JOIN path_info b ON a.path_name = b.path_info_name;"""

sspUtil_filter = """SELECT YEAR(reporting_date) AS years, MONTHNAME(reporting_date)AS months,
COUNT(IF(current_ssp_util < 40,1, null)) AS count_lt_forty,
COUNT(IF((current_ssp_util >= 40 AND current_ssp_util <= 49),1, null)) AS count_lt_fortynine,
COUNT(IF((current_ssp_util >= 50 AND current_ssp_util <= 59),1, null )) AS count_lt_fiftynine,
COUNT(IF((current_ssp_util >= 60 AND current_ssp_util <= 69),1, null )) AS count_lt_sixtynine,
COUNT(IF(current_ssp_util >= 70,1, null)) AS count_gt_seventy FROM dashboard_view
group BY YEAR(reporting_date), MONTHNAME(reporting_date);"""

wcfUtil_filter = """SELECT YEAR(reporting_date) AS years, MONTHNAME(reporting_date)AS months,
COUNT(IF(current_wcf_util < 70,1, null)) AS count_lt_seventy,
COUNT(IF((current_wcf_util >= 70 AND current_wcf_util <= 79),1, null)) AS count_lt_seventynine,
COUNT(IF((current_wcf_util >= 80 AND current_wcf_util <= 89),1, null )) AS count_lt_eightynine,
COUNT(IF((current_wcf_util >= 90 AND current_wcf_util <= 99),1, null )) AS count_lt_ninetynine,
COUNT(IF(current_wcf_util >= 100,1, null)) AS count_gt_hundred FROM dashboard_view
group BY YEAR(reporting_date), MONTHNAME(reporting_date);"""

augment_chart = """SELECT reporting_date, CONCAT(SUBSTRING(MONTHNAME(reporting_date),1,3),'-', YEAR(reporting_date)) AS path_date, ROUND(SUM(capacity_gbps)/1000,2) AS TotalValue FROM
dashboard_view WHERE reporting_date IS NOT null
GROUP BY reporting_date;"""


def WCFUtils(requests):
    wcfdata = [{
    'threshold': '<70%',
    'wcf_count': DashboardView.objects.filter(current_wcf_util__lt=70).count()
    },
    {
    'threshold': '70-79%',
    'wcf_count': DashboardView.objects.filter(current_wcf_util__range=(70,79)).count()
    },
    {
    'threshold': '80-89%',
    'wcf_count': DashboardView.objects.filter(current_wcf_util__range=(80,89)).count()
    },
    {
    'threshold': '90-99%',
    'wcf_count': DashboardView.objects.filter(current_wcf_util__range=(90,99)).count()
    },
    {
    'threshold': '>100%',
    'wcf_count': DashboardView.objects.filter(current_wcf_util__gte=100).count()
    },
    ]

    return JsonResponse(wcfdata, safe=False)

def SSPUtils(requests):
    sspdata = [{
     'threshold': '<40%',
     'ssp_count': DashboardView.objects.filter(current_ssp_util__lt=40).count()
     },
     {
     'threshold': '40-49%',
     'ssp_count': DashboardView.objects.filter(current_ssp_util__range=(40,49)).count()
     },
     {
     'threshold': '50-59%',
     'ssp_count': DashboardView.objects.filter(current_ssp_util__range=(50,59)).count()
     },
     {
     'threshold': '60-69%',
     'ssp_count': DashboardView.objects.filter(current_ssp_util__range=(60,69)).count()
     },
     {
     'threshold': '>70%',
     'ssp_count': DashboardView.objects.filter(current_ssp_util__gte=70).count()
     },
     ]

    return JsonResponse(sspdata, safe=False)

def CapacityAdded(requests):

    objects = AugmentEntryView.objects.all().extra(select={'month_stamp': 'MONTHNAME(reporting_date)'}).values('month_stamp').annotate(year_stamp= Extract('reporting_date', 'year')).values('month_stamp','year_stamp').annotate(total_augment=Sum('capacity_added_gbps'))
    objects_list = list(objects)
    for obj in objects_list:
        obj.update({'month_year':str(obj['month_stamp'])+','+str(obj['year_stamp'])})
        if obj['total_augment'] is not None:
            obj['total_augment'] = obj['total_augment']/1000


    return JsonResponse(objects_list, safe=False)

def AugmentCount(requests):

    objects = AugmentEntryView.objects.all().extra(select={'month_stamp': 'MONTHNAME(reporting_date)'}).values('month_stamp').annotate(year_stamp= Extract('reporting_date', 'year')).values('month_stamp','year_stamp').annotate(Count_augment=Count('capacity_added_gbps'))
    objects_list = list(objects)
    for obj in objects_list:
        obj.update({'month_year':str(obj['month_stamp'])+','+str(obj['year_stamp'])})

    return JsonResponse(objects_list, safe=False)

def TotalCapacity(requests):

    objects = AugmentEntryView.objects.all().extra(select={'month_stamp': 'MONTHNAME(reporting_date)'}).values('month_stamp').annotate(year_stamp= Extract('reporting_date', 'year')).values('month_stamp','year_stamp').annotate(total_capacity=Sum('ms_capacity_gbps'))
    objects_list = list(objects)
    for obj in objects_list:
        obj.update({'month_year':str(obj['month_stamp'])+','+str(obj['year_stamp'])})
        if obj['total_capacity'] is not None:
            obj['total_capacity'] = obj['total_capacity']/1000

    return JsonResponse(objects_list, safe=False)

def dashboardViewfilter(requests):

    # data =AugmentEntryView.objects.all().extra(select={'month_stamp': 'MONTHNAME(reporting_date)'}).values('month_stamp').annotate(year_stamp= Extract('reporting_date', 'year')).values('month_stamp','year_stamp').annotate(total_capacity=Sum('ms_capacity_gbps'))

    # obj_list = list(AugmentEntryView.objects.all().extra(select={'month_stamp': 'MONTHNAME(reporting_date)'}).values('month_stamp').annotate(year_stamp= Extract('reporting_date', 'year')).values('month_stamp','year_stamp').annotate(total_capacity=Sum('ms_capacity_gbps')))

    objects = AugmentEntryView.objects.all()
    for obj in objects:
        obj.path = obj.a_node+" - "+obj.z_node
    obj_list = list(objects)
    return JsonResponse(obj_list, safe=False)

def month_yearDV_filter(requests):

    c = connection.cursor()

    c.execute(sql_myfilter)

    desc = c.description

    column_names = [col[0] for col in desc]

    db_data = [dict(zip(column_names, row)) for row in c.fetchall()]

    c.close()

    return JsonResponse(db_data, safe=False)

def pathinfoDV_filter(requests):

    c = connection.cursor()

    c.execute(sql_pathinfo)

    desc = c.description

    column_names = [col[0] for col in desc]

    db_data = [dict(zip(column_names, row)) for row in c.fetchall()]

    c.close()

    return JsonResponse(db_data, safe=False)

def SSPUtils_filter(requests):

    c = connection.cursor()

    c.execute(sspUtil_filter)

    desc = c.description

    column_names = [col[0] for col in desc]

    db_data = [dict(zip(column_names, row)) for row in c.fetchall()]

    c.close()

    return JsonResponse(db_data, safe=False)

def WCFUtils_filter(requests):

    c = connection.cursor()

    c.execute(wcfUtil_filter)

    desc = c.description

    column_names = [col[0] for col in desc]

    db_data = [dict(zip(column_names, row)) for row in c.fetchall()]

    c.close()

    return JsonResponse(db_data, safe=False)


def NBBAugmentChart(requests):

    c = connection.cursor()

    c.execute(augment_chart)

    desc = c.description

    column_names = [col[0] for col in desc]

    db_data = [dict(zip(column_names, row)) for row in c.fetchall()]

    c.close()

    return JsonResponse(db_data, safe=False)
