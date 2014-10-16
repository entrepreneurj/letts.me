# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('links', '0006_auto_20141016_0600'),
    ]

    operations = [
        migrations.AlterField(
            model_name='link',
            name='date_submitted',
            field=models.DateTimeField(auto_now_add=True),
        ),
    ]
