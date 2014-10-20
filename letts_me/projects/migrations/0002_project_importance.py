# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('projects', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='project',
            name='importance',
            field=models.CharField(default=1, max_length=1, choices=[(1, b'Most Important'), (2, b'Average Importance'), (3, b'Least Important')]),
            preserve_default=True,
        ),
    ]
