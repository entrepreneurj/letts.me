# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('frontpage', '0002_auto_20141016_0600'),
        ('projects', '0002_project_importance'),
    ]

    operations = [
        migrations.AddField(
            model_name='project',
            name='categories',
            field=models.ManyToManyField(to='frontpage.Category', null=True, blank=True),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='project',
            name='completion',
            field=models.IntegerField(default=0),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='project',
            name='importance',
            field=models.CharField(default=b'2', max_length=1, choices=[(b'1', b'Most Important'), (b'2', b'Average Importance'), (b'3', b'Least Important')]),
        ),
    ]
