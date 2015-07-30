# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import datetime
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('bigdata', '0009_auto_20150713_1405'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='news',
            options={'verbose_name': '新闻'},
        ),
        migrations.AlterField(
            model_name='academic',
            name='time_stamp',
            field=models.DateTimeField(auto_now_add=True, default=datetime.datetime(2015, 7, 13, 6, 16, 21, 110238, tzinfo=utc)),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='join1',
            name='time_stamp',
            field=models.DateTimeField(auto_now_add=True, default=datetime.datetime(2015, 7, 13, 6, 16, 21, 110238, tzinfo=utc)),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='join2',
            name='time_stamp',
            field=models.DateTimeField(auto_now_add=True, default=datetime.datetime(2015, 7, 13, 6, 16, 21, 110238, tzinfo=utc)),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='meetings',
            name='time_stamp',
            field=models.DateTimeField(auto_now_add=True, default=datetime.datetime(2015, 7, 13, 6, 16, 21, 110238, tzinfo=utc)),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='news',
            name='time_stamp',
            field=models.DateTimeField(auto_now_add=True, default=datetime.datetime(2015, 7, 13, 6, 16, 21, 110238, tzinfo=utc)),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='notices',
            name='time_stamp',
            field=models.DateTimeField(auto_now_add=True, default=datetime.datetime(2015, 7, 13, 6, 16, 21, 110238, tzinfo=utc)),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='relax',
            name='time_stamp',
            field=models.DateTimeField(auto_now_add=True, default=datetime.datetime(2015, 7, 13, 6, 16, 21, 110238, tzinfo=utc)),
            preserve_default=True,
        ),
    ]
