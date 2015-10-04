from django.contrib.gis import admin
from .models import CallLocation, CallType


class GeoLocationAdmin(admin.OSMGeoAdmin):
    default_zoom = 11
    list_display = (
        'call_type', 'address',
        'timestamp', 'status_id')

admin.site.register(CallLocation, GeoLocationAdmin)
admin.site.register(CallType)
