# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('projects', '0006_auto_20141022_0318'),
    ]

    operations = [
        migrations.AlterField(
            model_name='project',
            name='demo_url',
            field=models.URLField(null=True, blank=True),
        ),
        migrations.AlterField(
            model_name='project',
            name='repo_url',
            field=models.URLField(null=True, blank=True),
        ),
    ]
