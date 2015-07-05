# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
from django.utils.timezone import utc
import datetime


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='News',
            fields=[
                ('id', models.AutoField(auto_created=True, serialize=False, primary_key=True, verbose_name='ID')),
                ('title', models.CharField(max_length=150, null=True)),
                ('content', models.TextField(null=True)),
                ('time_stamp', models.DateTimeField(default=datetime.datetime(2015, 7, 5, 10, 41, 36, 124854, tzinfo=utc), auto_now_add=True)),
                ('link', models.URLField(verbose_name='url_link', blank=True)),
            ],
            options={
                'abstract': False,
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='Postgraduate',
            fields=[
                ('id', models.AutoField(auto_created=True, serialize=False, primary_key=True, verbose_name='ID')),
                ('name', models.CharField(max_length=150, verbose_name='姓名')),
                ('Email', models.EmailField(max_length=75)),
                ('mainpage', models.URLField(verbose_name='个人主页', blank=True)),
                ('grade', models.CharField(max_length=1, verbose_name='年级')),
                ('educational_level', models.CharField(max_length=18, verbose_name='学位（博士/硕士）')),
            ],
            options={
                'abstract': False,
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='Professor',
            fields=[
                ('id', models.AutoField(auto_created=True, serialize=False, primary_key=True, verbose_name='ID')),
                ('name', models.CharField(max_length=150, verbose_name='姓名')),
                ('Email', models.EmailField(max_length=75)),
                ('mainpage', models.URLField(verbose_name='个人主页', blank=True)),
                ('job_title', models.CharField(max_length=150, verbose_name='职称', null=True)),
            ],
            options={
                'abstract': False,
            },
            bases=(models.Model,),
        ),
    ]
