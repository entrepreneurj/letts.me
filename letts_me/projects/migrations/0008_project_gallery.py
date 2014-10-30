# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('frontpage', '0005_auto_20141030_0401'),
        ('projects', '0007_auto_20141023_0406'),
    ]

    operations = [
        migrations.AddField(
            model_name='project',
            name='gallery',
            field=models.ForeignKey(blank=True, to='frontpage.Gallery', null=True),
            preserve_default=True,
        ),
    ]
