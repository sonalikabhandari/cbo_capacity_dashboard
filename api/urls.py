""" API routes """

from django.urls import path, re_path, include
from rest_framework.routers import DefaultRouter

from . import views

ROUTER = DefaultRouter()

urlpatterns = [
    path('', include(ROUTER.urls)),
]
