# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import datetime
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('bigdata', '0010_auto_20150713_1416'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='academic',
            options={'verbose_name': '学术交流活动'},
        ),
        migrations.AlterModelOptions(
            name='join1',
            options={'verbose_name': '招生信息'},
        ),
        migrations.AlterModelOptions(
            name='join2',
            options={'verbose_name': '人才招聘'},
        ),
        migrations.AlterModelOptions(
            name='lab',
            options={'verbose_name': '实验室相关信息'},
        ),
        migrations.AlterModelOptions(
            name='meetings',
            options={'verbose_name': '近期学术会议'},
        ),
        migrations.AlterModelOptions(
            name='news',
            options={'verbose_name': '新闻动态'},
        ),
        migrations.AlterModelOptions(
            name='notices',
            options={'verbose_name': '通知公告'},
        ),
        migrations.AlterModelOptions(
            name='postgraduate',
            options={'verbose_name': '学生信息'},
        ),
        migrations.AlterModelOptions(
            name='professor',
            options={'verbose_name': '老师信息'},
        ),
        migrations.AlterModelOptions(
            name='relax',
            options={'verbose_name': '休闲活动'},
        ),
        migrations.AlterField(
            model_name='academic',
            name='time_stamp',
            field=models.DateTimeField(default=datetime.datetime(2015, 7, 13, 6, 20, 14, 391447, tzinfo=utc), auto_now_add=True),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='join1',
            name='time_stamp',
            field=models.DateTimeField(default=datetime.datetime(2015, 7, 13, 6, 20, 14, 391447, tzinfo=utc), auto_now_add=True),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='join2',
            name='time_stamp',
            field=models.DateTimeField(default=datetime.datetime(2015, 7, 13, 6, 20, 14, 391447, tzinfo=utc), auto_now_add=True),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='meetings',
            name='time_stamp',
            field=models.DateTimeField(default=datetime.datetime(2015, 7, 13, 6, 20, 14, 391447, tzinfo=utc), auto_now_add=True),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='news',
            name='time_stamp',
            field=models.DateTimeField(default=datetime.datetime(2015, 7, 13, 6, 20, 14, 391447, tzinfo=utc), auto_now_add=True),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='notices',
            name='time_stamp',
            field=models.DateTimeField(default=datetime.datetime(2015, 7, 13, 6, 20, 14, 391447, tzinfo=utc), auto_now_add=True),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='relax',
            name='time_stamp',
            field=models.DateTimeField(default=datetime.datetime(2015, 7, 13, 6, 20, 14, 391447, tzinfo=utc), auto_now_add=True),
            preserve_default=True,
        ),
    ]
