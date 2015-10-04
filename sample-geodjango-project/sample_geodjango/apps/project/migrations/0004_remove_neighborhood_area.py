# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('project', '0003_neighborhood'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='neighborhood',
            name='area',
        ),
    ]
