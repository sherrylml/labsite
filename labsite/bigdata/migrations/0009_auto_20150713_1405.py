# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
from django.utils.timezone import utc
import datetime


class Migration(migrations.Migration):

    dependencies = [
        ('bigdata', '0008_auto_20150713_0024'),
    ]

    operations = [
        migrations.RenameField(
            model_name='pubinf',
            old_name='publish_infor',
            new_name='publish_info',
        ),
        migrations.RenameField(
            model_name='pubinf1',
            old_name='publish_infor',
            new_name='publish_info',
        ),
        migrations.RenameField(
            model_name='resact',
            old_name='research_activitiy',
            new_name='research_activity',
        ),
        migrations.RenameField(
            model_name='resact1',
            old_name='research_activitiy',
            new_name='research_activity',
        ),
        migrations.AlterField(
            model_name='academic',
            name='time_stamp',
            field=models.DateTimeField(auto_now_add=True, default=datetime.datetime(2015, 7, 13, 6, 4, 52, 524638, tzinfo=utc)),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='join1',
            name='time_stamp',
            field=models.DateTimeField(auto_now_add=True, default=datetime.datetime(2015, 7, 13, 6, 4, 52, 524638, tzinfo=utc)),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='join2',
            name='time_stamp',
            field=models.DateTimeField(auto_now_add=True, default=datetime.datetime(2015, 7, 13, 6, 4, 52, 524638, tzinfo=utc)),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='meetings',
            name='time_stamp',
            field=models.DateTimeField(auto_now_add=True, default=datetime.datetime(2015, 7, 13, 6, 4, 52, 524638, tzinfo=utc)),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='news',
            name='time_stamp',
            field=models.DateTimeField(auto_now_add=True, default=datetime.datetime(2015, 7, 13, 6, 4, 52, 524638, tzinfo=utc)),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='notices',
            name='time_stamp',
            field=models.DateTimeField(auto_now_add=True, default=datetime.datetime(2015, 7, 13, 6, 4, 52, 524638, tzinfo=utc)),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='relax',
            name='time_stamp',
            field=models.DateTimeField(auto_now_add=True, default=datetime.datetime(2015, 7, 13, 6, 4, 52, 524638, tzinfo=utc)),
            preserve_default=True,
        ),
    ]
