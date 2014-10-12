# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0001_initial'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='entry',
            options={'ordering': ['-publish_date']},
        ),
        migrations.RenameField(
            model_name='entry',
            old_name='published',
            new_name='publish_date',
        ),
    ]
