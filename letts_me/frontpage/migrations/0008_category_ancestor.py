# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('frontpage', '0007_auto_20141030_0653'),
    ]

    operations = [
        migrations.AddField(
            model_name='category',
            name='ancestor',
            field=models.ForeignKey(related_name=b'descendent', blank=True, to='frontpage.Category', null=True),
            preserve_default=True,
        ),
    ]
