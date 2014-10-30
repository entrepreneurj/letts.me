# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import datetime


class Migration(migrations.Migration):

    dependencies = [
        ('frontpage', '0004_auto_20141029_0422'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='gallery',
            options={'verbose_name_plural': 'galleries'},
        ),
        migrations.AddField(
            model_name='gallery',
            name='publish_date',
            field=models.DateTimeField(default=datetime.datetime(2014, 10, 30, 4, 1, 35, 701840), auto_now_add=True),
            preserve_default=False,
        ),
    ]
