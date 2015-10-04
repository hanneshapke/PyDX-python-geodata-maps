#!/usr/bin/python

import geocoder
"""Sample code to demonstrate geocoding"""

address = "70 NW Couch St, Portland, OR 97209"
result = geocoder.google(address)
print ("Your address: %s" % address)
print ("%s, %s" % (result.lng, result.lat))
print ("Location type: %s" % result.accuracy)
