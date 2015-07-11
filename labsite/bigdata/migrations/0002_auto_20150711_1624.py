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
            model_name='news',
            name='link',
        ),
        migrations.RemoveField(
            model_name='notices',
            name='link',
        ),
        migrations.AddField(
            model_name='news',
            name='picture',
            field=models.ImageField(verbose_name='照片', upload_to='', null=True, blank=True),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='notices',
            name='picture',
            field=models.ImageField(verbose_name='照片', upload_to='', null=True, blank=True),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='news',
            name='time_stamp',
            field=models.DateTimeField(default=datetime.datetime(2015, 7, 11, 8, 24, 43, 985611, tzinfo=utc), auto_now_add=True),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='notices',
            name='time_stamp',
            field=models.DateTimeField(default=datetime.datetime(2015, 7, 11, 8, 24, 43, 985611, tzinfo=utc), auto_now_add=True),
            preserve_default=True,
        ),
    ]
