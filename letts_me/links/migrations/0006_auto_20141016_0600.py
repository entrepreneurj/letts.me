# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('links', '0005_link_categories'),
    ]

    operations = [
        migrations.AlterField(
            model_name='link',
            name='categories',
            field=models.ManyToManyField(to=b'frontpage.Category', null=True, blank=True),
        ),
    ]
