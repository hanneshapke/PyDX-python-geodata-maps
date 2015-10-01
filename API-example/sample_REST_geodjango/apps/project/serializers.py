from .models import CallLocation
from rest_framework import serializers


class CallSerializer(serializers.ModelSerializer):
    call_type = serializers.StringRelatedField()

    class Meta:
        model = CallLocation
        fields = ('status_id', 'address', 'location',
                  'call_type', 'timestamp', 'comment')
