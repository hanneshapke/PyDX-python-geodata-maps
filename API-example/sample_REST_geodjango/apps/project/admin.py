from django.contrib.gis import admin
from .models import CallLocation, CallType


class GeoLocationAdmin(admin.OSMGeoAdmin):
    default_zoom = 11
    list_display = (
        'call_type', 'address',
        'modified',)

admin.site.register(CallLocation, GeoLocationAdmin)
admin.site.register(CallType)
