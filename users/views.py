from api.permissions import UserHasAdmin

from django.contrib.auth.models import Group
from django.shortcuts import get_object_or_404

from rest_framework import viewsets
from rest_framework.response import Response

from users.models import BulkPermissionStore, User

import logging
logger = logging.getLogger('django')

class BulkPermissionAdminHelper(viewsets.ViewSet):
    permission_classes = [UserHasAdmin]

    def list(self, request):
        departments = BulkPermissionStore.objects.all().order_by('department')
        groups = Group.objects.all().order_by('name')

        permissions = []

        for department in departments:
            settings = []
            bps_groups = department.groups.all()

            for group in groups:
                value = True if group in bps_groups else False
                settings.append({
                    'id': group.id,
                    'name': group.name,
                    'value': value
                })

            permissions.append({
                'id': department.id,
                'department': department.department,
                'settings' : settings
            })

        groups = list(groups.values_list('name', flat=True))

        return Response({
            'groups': groups,
            'permissions': permissions
        })

    def update (self, request, pk=None):
        bps = get_object_or_404(BulkPermissionStore.objects.all(), pk=pk)
        data = request.data
        settings = data.get('settings')
        for permission in settings:
            if permission.get('value'):
                bps.groups.add(permission.get('id'))
            else:
                bps.groups.remove(permission.get('id'))
        return Response({ 'data': 'ok' })


class UserAdminPermissionHelper(viewsets.ViewSet):
    permission_classes = [UserHasAdmin]

    def list(self, request):
        users = User.objects.filter(
            is_active=True, email__isnull=False
        ).order_by('first_name')
        groups = Group.objects.all().order_by('name')

        permissions = []

        for user in users:
            settings = []
            user_groups = user.groups.all()

            for group in groups:
                value = True if group in user_groups else False
                settings.append({
                    'id': group.id,
                    'name': group.name,
                    'value': value
                })

            permissions.append({
                'id': user.id,
                'user': f'{user.first_name} {user.last_name} - {user.username}',
                'settings': settings
            })

        groups = list(groups.values_list('name', flat=True))

        return Response({
            'groups': groups,
            'permissions': permissions
        })

    def update(self, request, pk=None):
        user = get_object_or_404(User.objects.all(), pk=pk)
        data = request.data
        settings = data.get('settings')
        for permission in settings:
            if permission.get('value'):
                user.groups.add(permission.get('id'))
            else:
                user.groups.remove(permission.get('id'))
        return Response({ 'data': 'ok' })
