# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('projects', '0005_auto_20141022_0315'),
    ]

    operations = [
        migrations.AlterField(
            model_name='project',
            name='repo_url',
            field=models.URLField(unique=True, null=True, blank=True),
        ),
    ]
