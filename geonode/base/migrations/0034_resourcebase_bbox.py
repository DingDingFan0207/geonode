# Migrating a new PolygonField (djnago GEOSGeometry) 'bbox'

import django.contrib.gis.db.models.fields
from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('base', '0033_auto_20200115_1145'),
    ]

    operations = [
        migrations.AddField(
            model_name='resourcebase',
            name='bbox',
            field=django.contrib.gis.db.models.fields.PolygonField(null=True, srid=4326),
        ),
    ]
