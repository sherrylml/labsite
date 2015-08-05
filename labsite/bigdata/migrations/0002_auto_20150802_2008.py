# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import datetime
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('bigdata', '0001_initial'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='lab',
            options={'verbose_name': '研究组相关信息'},
        ),
        migrations.AlterField(
            model_name='academic',
            name='time_stamp',
            field=models.DateTimeField(default=datetime.datetime(2015, 8, 2, 12, 8, 6, 188092, tzinfo=utc), auto_now_add=True),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='join1',
            name='time_stamp',
            field=models.DateTimeField(default=datetime.datetime(2015, 8, 2, 12, 8, 6, 188092, tzinfo=utc), auto_now_add=True),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='join2',
            name='time_stamp',
            field=models.DateTimeField(default=datetime.datetime(2015, 8, 2, 12, 8, 6, 188092, tzinfo=utc), auto_now_add=True),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='meetings',
            name='time_stamp',
            field=models.DateTimeField(default=datetime.datetime(2015, 8, 2, 12, 8, 6, 188092, tzinfo=utc), auto_now_add=True),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='news',
            name='time_stamp',
            field=models.DateTimeField(default=datetime.datetime(2015, 8, 2, 12, 8, 6, 188092, tzinfo=utc), auto_now_add=True),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='notices',
            name='time_stamp',
            field=models.DateTimeField(default=datetime.datetime(2015, 8, 2, 12, 8, 6, 188092, tzinfo=utc), auto_now_add=True),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='relax',
            name='time_stamp',
            field=models.DateTimeField(default=datetime.datetime(2015, 8, 2, 12, 8, 6, 188092, tzinfo=utc), auto_now_add=True),
            preserve_default=True,
        ),
    ]
