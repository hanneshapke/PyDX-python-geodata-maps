#!/usr/bin/python
"""Sample code to demonstrate motionless"""

import requests
from StringIO import StringIO
from PIL import Image
from slugify import slugify
from motionless import DecoratedMap, AddressMarker

address = "70 NW Couch St, Portland, OR 97209"
# generate static map object
dmap = DecoratedMap(
    maptype='satellite', zoom=18)
dmap.add_marker(
    AddressMarker(address))

# download the static image
response = requests.get(dmap.generate_url())
if response.status_code == 200:
    image = Image.open(StringIO(response.content))
    image.save('.'.join([slugify(address), 'png']))
else:
    print ("Download error with status code %s",
           response.status_code)
