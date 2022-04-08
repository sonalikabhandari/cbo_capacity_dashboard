from django.contrib import admin
from django.urls import path, re_path, include
from django.views.generic import TemplateView

from rest_framework_jwt.views import obtain_jwt_token, refresh_jwt_token

from .views import index

urlpatterns = [
    path('auth/obtain/', obtain_jwt_token),
    path('auth/refresh/', refresh_jwt_token),
    path('admin/', admin.site.urls),
    path('api/', include('api.urls')),
    path('reports/', include('reports.urls')),
    re_path(r'^.*$', index, name='index')
]
