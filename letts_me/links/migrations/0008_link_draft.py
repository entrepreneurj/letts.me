# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('links', '0007_auto_20141016_0607'),
    ]

    operations = [
        migrations.AddField(
            model_name='link',
            name='draft',
            field=models.BooleanField(default=False),
            preserve_default=True,
        ),
    ]
