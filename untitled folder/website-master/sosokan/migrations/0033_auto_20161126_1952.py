# -*- coding: utf-8 -*-
# Generated by Django 1.9.5 on 2016-11-27 00:52
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('sosokan', '0032_auto_20161126_1942'),
    ]

    operations = [
        migrations.AlterField(
            model_name='ad',
            name='createdAt',
            field=models.FloatField(default=1480207946.447),
        ),
        migrations.AlterField(
            model_name='ad',
            name='descendingTime',
            field=models.FloatField(default=-1480207946.447),
        ),
        migrations.AlterField(
            model_name='ad',
            name='updatedAt',
            field=models.FloatField(default=1480207946.447),
        ),
        migrations.AlterField(
            model_name='adimage',
            name='createdAt',
            field=models.FloatField(default=1480207946.449),
        ),
        migrations.AlterField(
            model_name='adimage',
            name='descendingTime',
            field=models.FloatField(default=-1480207946.449),
        ),
        migrations.AlterField(
            model_name='adimage',
            name='image',
            field=models.ImageField(height_field=b'height', upload_to=b'files/', width_field=b'width'),
        ),
        migrations.AlterField(
            model_name='adimage',
            name='updatedAt',
            field=models.FloatField(default=1480207946.449),
        ),
    ]