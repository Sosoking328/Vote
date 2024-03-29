# -*- coding: utf-8 -*-
# Generated by Django 1.9.6 on 2017-02-07 03:32
from __future__ import unicode_literals

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('sosokan', '0084_auto_20170206_2231'),
    ]

    operations = [
        migrations.AlterField(
            model_name='ad',
            name='createdAt',
            field=models.FloatField(default=1486438357.478),
        ),
        migrations.AlterField(
            model_name='ad',
            name='created_on',
            field=models.DateTimeField(default=datetime.datetime(2017, 2, 6, 22, 32, 37, 477000)),
        ),
        migrations.AlterField(
            model_name='ad',
            name='descendingTime',
            field=models.FloatField(default=-1486438357.477),
        ),
        migrations.AlterField(
            model_name='ad',
            name='updatedAt',
            field=models.FloatField(default=1486438357.478),
        ),
        migrations.AlterField(
            model_name='adimage',
            name='createdAt',
            field=models.FloatField(default=1486438357.479),
        ),
        migrations.AlterField(
            model_name='adimage',
            name='descendingTime',
            field=models.FloatField(default=-1486438357.479),
        ),
        migrations.AlterField(
            model_name='adimage',
            name='updatedAt',
            field=models.FloatField(default=1486438357.479),
        ),
        migrations.AlterField(
            model_name='categoryimage',
            name='createdAt',
            field=models.FloatField(default=1486438357.481),
        ),
        migrations.AlterField(
            model_name='categoryimage',
            name='descendingTime',
            field=models.FloatField(default=-1486438357.481),
        ),
        migrations.AlterField(
            model_name='categoryimage',
            name='updatedAt',
            field=models.FloatField(default=1486438357.481),
        ),
    ]
