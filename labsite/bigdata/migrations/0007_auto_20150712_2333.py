# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import datetime
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('bigdata', '0006_auto_20150712_2240'),
    ]

    operations = [
        migrations.AlterField(
            model_name='academic',
            name='time_stamp',
            field=models.DateTimeField(auto_now_add=True, default=datetime.datetime(2015, 7, 12, 15, 33, 39, 330872, tzinfo=utc)),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='join1',
            name='time_stamp',
            field=models.DateTimeField(auto_now_add=True, default=datetime.datetime(2015, 7, 12, 15, 33, 39, 330872, tzinfo=utc)),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='join2',
            name='time_stamp',
            field=models.DateTimeField(auto_now_add=True, default=datetime.datetime(2015, 7, 12, 15, 33, 39, 330872, tzinfo=utc)),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='meetings',
            name='time_stamp',
            field=models.DateTimeField(auto_now_add=True, default=datetime.datetime(2015, 7, 12, 15, 33, 39, 330872, tzinfo=utc)),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='news',
            name='time_stamp',
            field=models.DateTimeField(auto_now_add=True, default=datetime.datetime(2015, 7, 12, 15, 33, 39, 330872, tzinfo=utc)),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='notices',
            name='time_stamp',
            field=models.DateTimeField(auto_now_add=True, default=datetime.datetime(2015, 7, 12, 15, 33, 39, 330872, tzinfo=utc)),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='postgraduate',
            name='image',
            field=models.ImageField(verbose_name='个人照片', blank=True, upload_to='memberImg', null=True),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='professor',
            name='image',
            field=models.ImageField(verbose_name='个人照片', blank=True, upload_to='memberImg', null=True),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='relax',
            name='time_stamp',
            field=models.DateTimeField(auto_now_add=True, default=datetime.datetime(2015, 7, 12, 15, 33, 39, 330872, tzinfo=utc)),
            preserve_default=True,
        ),
    ]
