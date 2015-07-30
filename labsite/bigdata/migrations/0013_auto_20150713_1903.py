# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
from django.utils.timezone import utc
import datetime


class Migration(migrations.Migration):

    dependencies = [
        ('bigdata', '0012_auto_20150713_1858'),
    ]

    operations = [
        migrations.AlterField(
            model_name='academic',
            name='time_stamp',
            field=models.DateTimeField(auto_now_add=True, default=datetime.datetime(2015, 7, 13, 11, 3, 54, 212, tzinfo=utc)),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='join1',
            name='time_stamp',
            field=models.DateTimeField(auto_now_add=True, default=datetime.datetime(2015, 7, 13, 11, 3, 54, 212, tzinfo=utc)),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='join2',
            name='time_stamp',
            field=models.DateTimeField(auto_now_add=True, default=datetime.datetime(2015, 7, 13, 11, 3, 54, 212, tzinfo=utc)),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='meetings',
            name='time_stamp',
            field=models.DateTimeField(auto_now_add=True, default=datetime.datetime(2015, 7, 13, 11, 3, 54, 212, tzinfo=utc)),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='news',
            name='time_stamp',
            field=models.DateTimeField(auto_now_add=True, default=datetime.datetime(2015, 7, 13, 11, 3, 54, 212, tzinfo=utc)),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='notices',
            name='time_stamp',
            field=models.DateTimeField(auto_now_add=True, default=datetime.datetime(2015, 7, 13, 11, 3, 54, 212, tzinfo=utc)),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='postgraduate',
            name='grade',
            field=models.CharField(max_length=2, verbose_name='年级', choices=[('1', '1'), ('2', '2'), ('3', '3'), ('4', '4'), ('5', '5'), ('6', '6')]),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='relax',
            name='time_stamp',
            field=models.DateTimeField(auto_now_add=True, default=datetime.datetime(2015, 7, 13, 11, 3, 54, 212, tzinfo=utc)),
            preserve_default=True,
        ),
    ]
