#!/usr/bin/python

import geocoder
"""Sample code to demonstrate the ip geocoder
IP address obtained via http://fakeip.org/"""

ip_address = "192.169.226.73"
result = geocoder.ip(ip_address)
print ("Your ip address: %s" % ip_address)
print ("Location address: %s" % result.address)
print ("%s, %s" % (result.lng, result.lat))
