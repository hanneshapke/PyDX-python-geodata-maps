# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import django.contrib.gis.db.models.fields


class Migration(migrations.Migration):

    dependencies = [
        ('project', '0004_remove_neighborhood_area'),
    ]

    operations = [
        migrations.AlterField(
            model_name='neighborhood',
            name='poly',
            field=django.contrib.gis.db.models.fields.MultiPolygonField(srid=4326),
        ),
    ]
