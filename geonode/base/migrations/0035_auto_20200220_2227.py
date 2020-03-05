# Migrating the name of PolygonField 'bbox' into 'bbox_polygon'

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('base', '0034_resourcebase_bbox'),
    ]

    operations = [
        migrations.RenameField(
            model_name='resourcebase',
            old_name='bbox',
            new_name='bbox_polygon',
        ),
    ]
