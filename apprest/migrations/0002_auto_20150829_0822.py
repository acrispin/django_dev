# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('apprest', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='autor',
            name='apellido',
            field=models.CharField(max_length=100),
        ),
        migrations.AlterField(
            model_name='autor',
            name='nombre',
            field=models.CharField(max_length=100),
        ),
        migrations.AlterField(
            model_name='libro',
            name='editorial',
            field=models.CharField(max_length=100),
        ),
        migrations.AlterField(
            model_name='libro',
            name='genero',
            field=models.CharField(max_length=100),
        ),
        migrations.AlterField(
            model_name='libro',
            name='nombre',
            field=models.CharField(max_length=100),
        ),
    ]
