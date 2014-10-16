# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0003_auto_20141016_0556'),
    ]

    operations = [
        migrations.AlterField(
            model_name='entry',
            name='categories',
            field=models.ManyToManyField(to=b'frontpage.Category', null=True, blank=True),
        ),
    ]
