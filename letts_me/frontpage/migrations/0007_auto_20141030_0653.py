# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('frontpage', '0006_gallery_slug'),
    ]

    operations = [
        migrations.AlterField(
            model_name='gallery',
            name='slug',
            field=models.SlugField(),
        ),
    ]
