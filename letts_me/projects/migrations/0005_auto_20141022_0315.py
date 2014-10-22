# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('projects', '0004_auto_20141021_0519'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='project',
            options={'ordering': ['importance']},
        ),
        migrations.AddField(
            model_name='project',
            name='demo_url',
            field=models.URLField(unique=True, null=True, blank=True),
            preserve_default=True,
        ),
    ]
