# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import django_extensions.db.fields
import django.contrib.gis.db.models.fields


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='CallLocation',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('created', django_extensions.db.fields.CreationDateTimeField(auto_now_add=True, verbose_name='created')),
                ('modified', django_extensions.db.fields.ModificationDateTimeField(auto_now=True, verbose_name='modified')),
                ('address', models.CharField(max_length=255)),
                ('comment', models.TextField(null=True, blank=True)),
                ('status_id', models.CharField(max_length=20)),
                ('timestamp', models.DateTimeField(null=True, blank=True)),
                ('location', django.contrib.gis.db.models.fields.PointField(srid=4326)),
            ],
            options={
                'ordering': ['-modified'],
                'verbose_name_plural': 'Emergency Call Locations',
            },
        ),
        migrations.CreateModel(
            name='CallType',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('created', django_extensions.db.fields.CreationDateTimeField(auto_now_add=True, verbose_name='created')),
                ('modified', django_extensions.db.fields.ModificationDateTimeField(auto_now=True, verbose_name='modified')),
                ('name', models.CharField(max_length=50)),
            ],
            options={
                'ordering': ['-modified'],
                'verbose_name_plural': 'Call Types',
            },
        ),
        migrations.AddField(
            model_name='calllocation',
            name='call_type',
            field=models.ForeignKey(blank=True, to='project.CallType', null=True),
        ),
    ]
