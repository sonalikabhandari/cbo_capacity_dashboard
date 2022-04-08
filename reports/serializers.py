from rest_framework import serializers
from .models import *

class AugmentEntryViewSerializer(serializers.ModelSerializer):
    class Meta:
        model = AugmentEntryView
        fields = '__all__'

class DashboardViewSerializer(serializers.ModelSerializer):
    class Meta:
        model = DashboardView
        fields = '__all__'

class AugmentEntriesSerializer(serializers.ModelSerializer):
    class Meta:
        model = AugmentEntries
        fields = '__all__'

class CurrentCapacitySerializer(serializers.ModelSerializer):
    class Meta:
        model = CurrentCapacity
        fields = '__all__'

class LocationSerializer(serializers.ModelSerializer):
    class Meta:
        model = Location
        fields = '__all__'

class NodeSerializer(serializers.ModelSerializer):
    class Meta:
        model = Node
        fields = '__all__'

class PathSerializer(serializers.ModelSerializer):
    class Meta:
        model = Path
        fields = '__all__'

class TrafficInfoSerializer(serializers.ModelSerializer):
    class Meta:
        model = TrafficInfo
        fields = '__all__'