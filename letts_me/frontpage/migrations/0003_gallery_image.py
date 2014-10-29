# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import frontpage.models


class Migration(migrations.Migration):

    dependencies = [
        ('frontpage', '0002_auto_20141016_0600'),
    ]

    operations = [
        migrations.CreateModel(
            name='Gallery',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('title', models.CharField(max_length=30)),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='Image',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('img_file', models.ImageField(upload_to=frontpage.models.upload_path)),
                ('title', models.CharField(max_length=30, blank=True)),
                ('description', models.CharField(max_length=140, blank=True)),
                ('gallery', models.ForeignKey(to='frontpage.Gallery')),
            ],
            options={
            },
            bases=(models.Model,),
        ),
    ]
