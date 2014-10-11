# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Entry',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('title', models.CharField(max_length=100)),
                ('slug', models.SlugField()),
                ('text', models.TextField()),
                ('draft', models.BooleanField(default=True)),
                ('published', models.DateTimeField(auto_now_add=True)),
            ],
            options={
                'ordering': ['-published'],
            },
            bases=(models.Model,),
        ),
    ]
