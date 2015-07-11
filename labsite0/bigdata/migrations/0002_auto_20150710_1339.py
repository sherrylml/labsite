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
        migrations.AlterField(
            model_name='news',
            name='time_stamp',
            field=models.DateTimeField(auto_now_add=True, default=datetime.datetime(2015, 7, 10, 5, 39, 40, 64688, tzinfo=utc)),
            preserve_default=True,
        ),
    ]
