import sys

from django.contrib.gis.db import models
from django.contrib.gis.geos import fromstr
from django_extensions.db.models import TimeStampedModel

import geocoder


class Neighborhood(models.Model):
    name = models.CharField(max_length=100)
    poly = models.MultiPolygonField()
    objects = models.GeoManager()

    class Meta:
        ordering = ['name']
        verbose_name_plural = "Portland Neighborhoods"

    def __unicode__(self):
        return self.name


class CallType(TimeStampedModel):

    name = models.CharField(max_length=50)

    class Meta:
        ordering = ['-modified']
        verbose_name_plural = "Call Types"

    # Returns the string representation of the model.
    def __unicode__(self):
        return '%s' % (self.name)


class CallLocation(TimeStampedModel):

    address = models.CharField(
        max_length=255)
    comment = models.TextField(
        blank=True, null=True)
    call_type = models.ForeignKey(
        CallType, blank=True, null=True)

    # GeoDjango-specific: a geometry field (PointField), and
    # overriding the default manager with a GeoManager instance.
    location = models.PointField()
    objects = models.GeoManager()

    class Meta:
        ordering = ['-modified']
        verbose_name_plural = "Emergency Call Locations"

    def save(self, *args, **kwargs):
        try:
            # get the geocoding results
            result = geocoder.google(self.address)
            # correct the address spelling by using the normalized address
            self.address = result.address.encode('utf-8')
            self.location = fromstr(
                'POINT(%s %s)' % (result.lng, result.lat),
                srid=4326)
        except (AttributeError, Exception):
            print "Oops!  Couldn't geocode address because of %s" \
                % sys.exc_info()[0]

        super(CallLocation, self).save(*args, **kwargs)

    # Returns the string representation of the model.
    def __unicode__(self):
        return '%s call from %s' % (self.call_type, self.address)
