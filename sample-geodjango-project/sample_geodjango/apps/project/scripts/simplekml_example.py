""" Example code which will generate a kml file of
Portland's neighborhoods

Execute this script with the runscript command
of the Django extensions
$ python manage.py runscript simplekml_example -v3
"""

import simplekml
from project.models import Neighborhood


def run():
    kml = simplekml.Kml()
    neighborhoods = Neighborhood.objects.all()

    for neighborhood in neighborhoods:
        # this is just bare example
        # normally use neighborhood.poly.kml to the kml data
        kml.newpolygon(
            name=neighborhood.name,
            outerboundaryis=list(
                neighborhood.poly.boundary.coords[0]),
            innerboundaryis=list(
                neighborhood.poly.boundary.coords[0])
        )
    kml.save("portland_neighborhoods.kml")
