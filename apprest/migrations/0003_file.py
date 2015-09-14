# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('apprest', '0002_auto_20150829_0822'),
    ]

    operations = [
        migrations.CreateModel(
            name='File',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('pathfile', models.FileField(upload_to=b'/home/anton/code/python/basedev/files')),
                ('reg_date', models.DateTimeField(auto_now_add=True, null=True)),
                ('mod_date', models.DateTimeField(auto_now=True, null=True)),
            ],
        ),
    ]
