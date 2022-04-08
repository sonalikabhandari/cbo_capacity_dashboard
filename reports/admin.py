
from django.contrib import admin
from .models import *

# Register your models here.

admin.site.register(AugmentEntries)
admin.site.register(Path)
admin.site.register(Location)
admin.site.register(Node)
admin.site.register(TrafficInfo)
admin.site.register(CurrentCapacity)
admin.site.register(AugmentEntryView)
admin.site.register(DashboardView)
