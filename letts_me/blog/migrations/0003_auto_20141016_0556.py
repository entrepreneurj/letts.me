# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('frontpage', '0001_initial'),
        ('blog', '0002_auto_20141012_0105'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='entry',
            options={'ordering': ['-publish_date'], 'verbose_name_plural': 'entries'},
        ),
        migrations.AddField(
            model_name='entry',
            name='categories',
            field=models.ManyToManyField(to='frontpage.Category'),
            preserve_default=True,
        ),
    ]
