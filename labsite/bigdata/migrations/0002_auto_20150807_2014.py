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
            name='academicen',
            options={'verbose_name': '学术交流活动(English)'},
        ),
        migrations.AlterModelOptions(
            name='join1en',
            options={'verbose_name': '招生信息(English)'},
        ),
        migrations.AlterModelOptions(
            name='join2en',
            options={'verbose_name': '人才招聘(English)'},
        ),
        migrations.AlterModelOptions(
            name='laben',
            options={'verbose_name': '研究组相关信息(English)'},
        ),
        migrations.AlterModelOptions(
            name='meetingsen',
            options={'verbose_name': '近期学术会议(English)'},
        ),
        migrations.AlterModelOptions(
            name='newsen',
            options={'verbose_name': '新闻动态(English)'},
        ),
        migrations.AlterModelOptions(
            name='noticesen',
            options={'verbose_name': '通知公告(English)'},
        ),
        migrations.AlterModelOptions(
            name='postgraduateen',
            options={'verbose_name': '学生信息(English)'},
        ),
        migrations.AlterModelOptions(
            name='professoren',
            options={'verbose_name': '老师信息(English)'},
        ),
        migrations.AlterModelOptions(
            name='relaxen',
            options={'verbose_name': '休闲活动(English)'},
        ),
        migrations.AlterField(
            model_name='academic',
            name='time_stamp',
            field=models.DateTimeField(default=datetime.datetime(2015, 8, 7, 12, 14, 45, 684420, tzinfo=utc), auto_now_add=True),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='academicen',
            name='time_stamp',
            field=models.DateTimeField(default=datetime.datetime(2015, 8, 7, 12, 14, 45, 695432, tzinfo=utc), auto_now_add=True),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='join1',
            name='time_stamp',
            field=models.DateTimeField(default=datetime.datetime(2015, 8, 7, 12, 14, 45, 684420, tzinfo=utc), auto_now_add=True),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='join1en',
            name='time_stamp',
            field=models.DateTimeField(default=datetime.datetime(2015, 8, 7, 12, 14, 45, 695432, tzinfo=utc), auto_now_add=True),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='join2',
            name='time_stamp',
            field=models.DateTimeField(default=datetime.datetime(2015, 8, 7, 12, 14, 45, 684420, tzinfo=utc), auto_now_add=True),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='join2en',
            name='time_stamp',
            field=models.DateTimeField(default=datetime.datetime(2015, 8, 7, 12, 14, 45, 695432, tzinfo=utc), auto_now_add=True),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='meetings',
            name='time_stamp',
            field=models.DateTimeField(default=datetime.datetime(2015, 8, 7, 12, 14, 45, 684420, tzinfo=utc), auto_now_add=True),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='meetingsen',
            name='time_stamp',
            field=models.DateTimeField(default=datetime.datetime(2015, 8, 7, 12, 14, 45, 695432, tzinfo=utc), auto_now_add=True),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='news',
            name='time_stamp',
            field=models.DateTimeField(default=datetime.datetime(2015, 8, 7, 12, 14, 45, 684420, tzinfo=utc), auto_now_add=True),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='newsen',
            name='time_stamp',
            field=models.DateTimeField(default=datetime.datetime(2015, 8, 7, 12, 14, 45, 695432, tzinfo=utc), auto_now_add=True),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='notices',
            name='time_stamp',
            field=models.DateTimeField(default=datetime.datetime(2015, 8, 7, 12, 14, 45, 684420, tzinfo=utc), auto_now_add=True),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='noticesen',
            name='time_stamp',
            field=models.DateTimeField(default=datetime.datetime(2015, 8, 7, 12, 14, 45, 695432, tzinfo=utc), auto_now_add=True),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='relax',
            name='time_stamp',
            field=models.DateTimeField(default=datetime.datetime(2015, 8, 7, 12, 14, 45, 684420, tzinfo=utc), auto_now_add=True),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='relaxen',
            name='time_stamp',
            field=models.DateTimeField(default=datetime.datetime(2015, 8, 7, 12, 14, 45, 695432, tzinfo=utc), auto_now_add=True),
            preserve_default=True,
        ),
    ]
