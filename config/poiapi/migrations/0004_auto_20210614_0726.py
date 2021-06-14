# Generated by Django 3.1.5 on 2021-06-14 07:26

import django.contrib.gis.db.models.fields
import django.contrib.gis.geos.point
from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('poiapi', '0003_auto_20210614_0715'),
    ]

    operations = [
        migrations.AlterField(
            model_name='pointofinterest',
            name='location',
            field=django.contrib.gis.db.models.fields.PointField(default=django.contrib.gis.geos.point.Point(106.7264194085899, -6.555760409044816), geography=True, srid=4326),
        ),
    ]
