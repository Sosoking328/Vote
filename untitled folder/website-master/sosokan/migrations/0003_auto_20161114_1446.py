# -*- coding: utf-8 -*-
# Generated by Django 1.9.5 on 2016-11-14 19:46
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('sosokan', '0002_auto_20161114_1400'),
    ]

    operations = [
        migrations.AddField(
            model_name='ad',
            name='address',
            field=models.CharField(default=b'', max_length=255),
        ),
        migrations.AddField(
            model_name='ad',
            name='advertiseId',
            field=models.CharField(default=b'', max_length=255),
        ),
        migrations.AddField(
            model_name='ad',
            name='categoryId',
            field=models.CharField(default=b'', max_length=255),
        ),
        migrations.AddField(
            model_name='ad',
            name='chinese',
            field=models.BooleanField(default=None),
        ),
        migrations.AddField(
            model_name='ad',
            name='coupon',
            field=models.CharField(default=b'', max_length=255),
        ),
        migrations.AddField(
            model_name='ad',
            name='createdAt',
            field=models.CharField(default=b'', max_length=255),
        ),
        migrations.AddField(
            model_name='ad',
            name='descendingTime',
            field=models.CharField(default=b'', max_length=255),
        ),
        migrations.AddField(
            model_name='ad',
            name='description',
            field=models.TextField(default=b''),
        ),
        migrations.AddField(
            model_name='ad',
            name='descriptionPlainText',
            field=models.TextField(default=b''),
        ),
        migrations.AddField(
            model_name='ad',
            name='enableEmail',
            field=models.BooleanField(default=None),
        ),
        migrations.AddField(
            model_name='ad',
            name='enablePhone',
            field=models.BooleanField(default=None),
        ),
        migrations.AddField(
            model_name='ad',
            name='feature',
            field=models.BooleanField(default=None),
        ),
        migrations.AddField(
            model_name='ad',
            name='flagCount',
            field=models.IntegerField(default=None),
        ),
        migrations.AddField(
            model_name='ad',
            name='hidden',
            field=models.BooleanField(default=None),
        ),
        migrations.AddField(
            model_name='ad',
            name='isChinese',
            field=models.BooleanField(default=None),
        ),
        migrations.AddField(
            model_name='ad',
            name='isFeatured',
            field=models.BooleanField(default=None),
        ),
        migrations.AddField(
            model_name='ad',
            name='isHtmlDes',
            field=models.BooleanField(default=None),
        ),
        migrations.AddField(
            model_name='ad',
            name='isStandout',
            field=models.BooleanField(default=None),
        ),
        migrations.AddField(
            model_name='ad',
            name='legacy_id',
            field=models.TextField(default=b'', max_length=255),
        ),
        migrations.AddField(
            model_name='ad',
            name='name',
            field=models.CharField(default=b'', max_length=255),
        ),
        migrations.AddField(
            model_name='ad',
            name='price',
            field=models.DecimalField(decimal_places=2, default=0, max_digits=8),
        ),
        migrations.AddField(
            model_name='ad',
            name='saleOff',
            field=models.TextField(default=b'', max_length=255),
        ),
        migrations.AddField(
            model_name='ad',
            name='shareCount',
            field=models.TextField(default=b'', max_length=255),
        ),
        migrations.AddField(
            model_name='ad',
            name='standout',
            field=models.BooleanField(default=None),
        ),
        migrations.AddField(
            model_name='ad',
            name='userId',
            field=models.CharField(default=b'', max_length=255),
        ),
    ]
