# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import datetime
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('bigdata', '0002_auto_20150802_2008'),
    ]

    operations = [
        migrations.AlterField(
            model_name='academic',
            name='time_stamp',
            field=models.DateTimeField(default=datetime.datetime(2015, 8, 2, 13, 6, 55, 469221, tzinfo=utc), auto_now_add=True),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='images',
            name='images',
            field=models.ImageField(null=True, verbose_name='图片', blank=True, upload_to='research_direction'),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='join1',
            name='time_stamp',
            field=models.DateTimeField(default=datetime.datetime(2015, 8, 2, 13, 6, 55, 469221, tzinfo=utc), auto_now_add=True),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='join2',
            name='time_stamp',
            field=models.DateTimeField(default=datetime.datetime(2015, 8, 2, 13, 6, 55, 469221, tzinfo=utc), auto_now_add=True),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='meetings',
            name='time_stamp',
            field=models.DateTimeField(default=datetime.datetime(2015, 8, 2, 13, 6, 55, 469221, tzinfo=utc), auto_now_add=True),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='news',
            name='time_stamp',
            field=models.DateTimeField(default=datetime.datetime(2015, 8, 2, 13, 6, 55, 469221, tzinfo=utc), auto_now_add=True),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='notices',
            name='time_stamp',
            field=models.DateTimeField(default=datetime.datetime(2015, 8, 2, 13, 6, 55, 469221, tzinfo=utc), auto_now_add=True),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='relax',
            name='time_stamp',
            field=models.DateTimeField(default=datetime.datetime(2015, 8, 2, 13, 6, 55, 469221, tzinfo=utc), auto_now_add=True),
            preserve_default=True,
        ),
    ]
