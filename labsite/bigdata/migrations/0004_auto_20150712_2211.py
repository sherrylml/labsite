# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import datetime
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('bigdata', '0003_auto_20150712_2151'),
    ]

    operations = [
        migrations.AlterField(
            model_name='academic',
            name='time_stamp',
            field=models.DateTimeField(auto_now_add=True, default=datetime.datetime(2015, 7, 12, 14, 11, 43, 313458, tzinfo=utc)),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='join1',
            name='time_stamp',
            field=models.DateTimeField(auto_now_add=True, default=datetime.datetime(2015, 7, 12, 14, 11, 43, 313458, tzinfo=utc)),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='join2',
            name='time_stamp',
            field=models.DateTimeField(auto_now_add=True, default=datetime.datetime(2015, 7, 12, 14, 11, 43, 313458, tzinfo=utc)),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='meetings',
            name='time_stamp',
            field=models.DateTimeField(auto_now_add=True, default=datetime.datetime(2015, 7, 12, 14, 11, 43, 313458, tzinfo=utc)),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='news',
            name='time_stamp',
            field=models.DateTimeField(auto_now_add=True, default=datetime.datetime(2015, 7, 12, 14, 11, 43, 313458, tzinfo=utc)),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='notices',
            name='time_stamp',
            field=models.DateTimeField(auto_now_add=True, default=datetime.datetime(2015, 7, 12, 14, 11, 43, 313458, tzinfo=utc)),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='relax',
            name='time_stamp',
            field=models.DateTimeField(auto_now_add=True, default=datetime.datetime(2015, 7, 12, 14, 11, 43, 313458, tzinfo=utc)),
            preserve_default=True,
        ),
    ]
