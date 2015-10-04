from django.contrib.gis import admin
from .models import CallLocation, CallType, Neighborhood


class GeoLocationAdmin(admin.OSMGeoAdmin):
    default_zoom = 11
    list_display = (
        'call_type', 'address',
        'modified',)


class NeighboorhoodAdmin(admin.OSMGeoAdmin):
    default_zoom = 11
    list_display = ('name',)

admin.site.register(CallLocation, GeoLocationAdmin)
admin.site.register(Neighborhood, NeighboorhoodAdmin)
admin.site.register(CallType)
