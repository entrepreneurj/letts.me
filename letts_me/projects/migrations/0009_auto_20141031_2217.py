# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('projects', '0008_project_gallery'),
    ]

    operations = [
        migrations.AlterField(
            model_name='project',
            name='importance',
            field=models.CharField(default=b'2', max_length=1, choices=[(b'0', b'Featured'), (b'1', b'Most Important'), (b'2', b'Average Importance'), (b'3', b'Least Important')]),
        ),
    ]
