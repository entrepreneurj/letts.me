# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('frontpage', '0003_gallery_image'),
    ]

    operations = [
        migrations.AlterField(
            model_name='gallery',
            name='title',
            field=models.CharField(max_length=50),
        ),
    ]
