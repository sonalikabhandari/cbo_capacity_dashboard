from django.urls import path, include
from reports import views
from django.contrib import admin
from rest_framework import routers

from django.conf.urls import url

app_name = 'reports'

router = routers.DefaultRouter()

router.register('node', views.NodeAPI, basename='node')
router.register('path', views.PathAPI, basename='path')
router.register('traffic_info', views.TrafficInfoAPI, basename='traffic_info')
router.register('location', views.LocationAPI, basename='location')
router.register('augment_entries', views.AugmentEntriesAPI, basename='augment_entries')
router.register('current_capacity', views.CurrentCapacityAPI, basename='current_capacity')
router.register('dashboardview', views.DashboardViewAPI, basename='dashboardview')
router.register('augmentview', views.AugmentEntryViewAPI, basename='augmentview')
urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include(router.urls)),
    url(r'^wcfutils/$', views.WCFUtils, name='wcf_util'),
    url(r'^ssputils/$', views.SSPUtils, name='ssp_util'),
    url(r'^augmentadded/$', views.CapacityAdded, name='capacity_added'),
    url(r'^augmentcount/$', views.AugmentCount, name='augment_count'),
    url(r'^totalcurrentcapacity/$', views.TotalCapacity, name='augment_capacity'),
    url(r'^dashboardviewfilterMY/$', views.month_yearDV_filter, name='dashboardview_MYfilter'),
    url(r'^dashboardviewPathinfo/$', views.pathinfoDV_filter, name='dashboardview_pathinfo'),
    url(r'^SSPUtilfilter/$', views.SSPUtils_filter, name='ssp_util'),
    url(r'^WCFUtilfilter/$', views.WCFUtils_filter, name='wcf_util'),
    url(r'^augmentChart/$', views.NBBAugmentChart, name='NBB_Chart'),
]
