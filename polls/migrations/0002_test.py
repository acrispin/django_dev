# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('polls', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Test',
            fields=[
                ('iden', models.IntegerField(serialize=False, primary_key=True)),
                ('code', models.CharField(unique=True, max_length=4)),
                ('name', models.CharField(max_length=50, db_column=b'fullname')),
                ('period', models.CharField(max_length=6, db_index=True)),
                ('dni', models.CharField(max_length=8, blank=True)),
                ('email', models.EmailField(max_length=75, null=True)),
                ('comments', models.TextField(null=True)),
                ('num', models.IntegerField(default=0, null=True)),
                ('cost', models.DecimalField(null=True, max_digits=8, decimal_places=2)),
                ('vent', models.DecimalField(null=True, max_digits=13, decimal_places=4)),
                ('total', models.FloatField(null=True)),
                ('sec', models.SmallIntegerField(null=True)),
                ('big', models.BigIntegerField(null=True)),
                ('flag', models.NullBooleanField()),
                ('active', models.BooleanField(default=True)),
                ('cum_date', models.DateField(null=True)),
                ('reg_date', models.DateTimeField(auto_now_add=True, null=True)),
                ('reg_user', models.CharField(max_length=30, null=True)),
                ('mod_date', models.DateTimeField(auto_now=True, null=True)),
                ('mod_user', models.CharField(max_length=30, null=True)),
            ],
        ),
    ]
