from . import views

from django.urls import path, include
from rest_framework.routers import DefaultRouter

router = DefaultRouter()

router.register('bps_admin', views.BulkPermissionAdminHelper, 'bps_admin')
router.register('user_admin', views.UserAdminPermissionHelper, 'user_admin')

urlpatterns = [
    path('', include(router.urls)),
]
