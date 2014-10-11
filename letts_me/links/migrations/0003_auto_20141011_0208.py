# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('links', '0002_auto_20141011_0018'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='link',
            options={'ordering': ['-date_submitted']},
        ),
        migrations.RenameField(
            model_name='link',
            old_name='date_sumbitted',
            new_name='date_submitted',
        ),
    ]
