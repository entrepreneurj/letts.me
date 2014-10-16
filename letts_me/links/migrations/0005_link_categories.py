# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('frontpage', '0001_initial'),
        ('links', '0004_link_blog_entry'),
    ]

    operations = [
        migrations.AddField(
            model_name='link',
            name='categories',
            field=models.ManyToManyField(to='frontpage.Category'),
            preserve_default=True,
        ),
    ]
