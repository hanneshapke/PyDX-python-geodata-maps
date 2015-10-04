from .models import CallLocation
from rest_framework import serializers
from rest_framework_gis import serializers as gis_serializer


class CallSerializer(gis_serializer.GeoModelSerializer):

    call_type = serializers.StringRelatedField()

    class Meta:
        model = CallLocation
        fields = ('status_id', 'address', 'location',
                  'call_type', 'timestamp')
        geo_field = 'point'
