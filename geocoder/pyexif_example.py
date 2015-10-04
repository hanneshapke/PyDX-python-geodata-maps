#!/usr/bin/python

from pyexif import pyexif
"""Sample code to demonstrate pyexif"""

file_name = "/Users/hannes/Downloads/IMG_6510.JPG"
exif_data = pyexif.get_exif_data(file_name)
result = pyexif.get_lat_lon(exif_data)

print ("Your location: %s" % result)
