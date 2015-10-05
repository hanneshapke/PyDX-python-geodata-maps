import os
from django.contrib.gis.utils import LayerMapping
from .models import Neighborhood

neighboorhood_mapping = {
    'name': 'NAME',
    'poly': 'POLYGON',
}

neighboorhood_shp = os.path.abspath(
    os.path.join(
        os.path.dirname(__file__),
        '../../data', 'neighborhoods.shp'))


def run(verbose=True):
    lm = LayerMapping(
        Neighborhood,
        neighboorhood_shp, neighboorhood_mapping,
        transform=False, encoding='iso-8859-1')
    lm.save(strict=True, verbose=verbose)
