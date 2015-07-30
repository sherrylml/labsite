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
        migrations.RemoveField(
            model_name='postgraduate',
            name='patent_prizes',
        ),
        migrations.RemoveField(
            model_name='postgraduate',
            name='publish_infors',
        ),
        migrations.RemoveField(
            model_name='postgraduate',
            name='research_activities',
        ),
        migrations.RemoveField(
            model_name='postgraduate',
            name='work_experiences',
        ),
        migrations.RemoveField(
            model_name='professor',
            name='patent_prizes',
        ),
        migrations.DeleteModel(
            name='PatPri',
        ),
        migrations.RemoveField(
            model_name='professor',
            name='publish_infors',
        ),
        migrations.RemoveField(
            model_name='professor',
            name='research_activities',
        ),
        migrations.RemoveField(
            model_name='professor',
            name='work_experiences',
        ),
        migrations.DeleteModel(
            name='PubInf',
        ),
        migrations.DeleteModel(
            name='ResAct',
        ),
        migrations.RemoveField(
            model_name='resdir',
            name='postgraduate',
        ),
        migrations.DeleteModel(
            name='Postgraduate',
        ),
        migrations.RemoveField(
            model_name='resdir',
            name='professor',
        ),
        migrations.DeleteModel(
            name='Professor',
        ),
        migrations.DeleteModel(
            name='ResDir',
        ),
        migrations.DeleteModel(
            name='WorkExp',
        ),
        migrations.AlterField(
            model_name='academic',
            name='time_stamp',
            field=models.DateTimeField(default=datetime.datetime(2015, 7, 12, 13, 50, 37, 872706, tzinfo=utc), auto_now_add=True),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='join1',
            name='time_stamp',
            field=models.DateTimeField(default=datetime.datetime(2015, 7, 12, 13, 50, 37, 872706, tzinfo=utc), auto_now_add=True),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='join2',
            name='time_stamp',
            field=models.DateTimeField(default=datetime.datetime(2015, 7, 12, 13, 50, 37, 872706, tzinfo=utc), auto_now_add=True),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='meetings',
            name='time_stamp',
            field=models.DateTimeField(default=datetime.datetime(2015, 7, 12, 13, 50, 37, 872706, tzinfo=utc), auto_now_add=True),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='news',
            name='time_stamp',
            field=models.DateTimeField(default=datetime.datetime(2015, 7, 12, 13, 50, 37, 872706, tzinfo=utc), auto_now_add=True),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='notices',
            name='time_stamp',
            field=models.DateTimeField(default=datetime.datetime(2015, 7, 12, 13, 50, 37, 872706, tzinfo=utc), auto_now_add=True),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='relax',
            name='time_stamp',
            field=models.DateTimeField(default=datetime.datetime(2015, 7, 12, 13, 50, 37, 872706, tzinfo=utc), auto_now_add=True),
            preserve_default=True,
        ),
    ]
