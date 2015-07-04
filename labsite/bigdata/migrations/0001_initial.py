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
            name='LearningMaterials',
            fields=[
                ('id', models.AutoField(serialize=False, auto_created=True, verbose_name='ID', primary_key=True)),
                ('title', models.CharField(null=True, max_length=150)),
                ('content', models.TextField(null=True)),
                ('time_stamp', models.DateTimeField(auto_now_add=True, default=datetime.datetime(2015, 7, 4, 15, 20, 9, 798316, tzinfo=utc))),
                ('link', models.URLField(blank=True, verbose_name='url_link')),
                ('introduction', models.TextField()),
                ('download_link', models.URLField()),
            ],
            options={
                'abstract': False,
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='News',
            fields=[
                ('id', models.AutoField(serialize=False, auto_created=True, verbose_name='ID', primary_key=True)),
                ('title', models.CharField(null=True, max_length=150)),
                ('content', models.TextField(null=True)),
                ('time_stamp', models.DateTimeField(auto_now_add=True, default=datetime.datetime(2015, 7, 4, 15, 20, 9, 798316, tzinfo=utc))),
                ('link', models.URLField(blank=True, verbose_name='url_link')),
            ],
            options={
                'abstract': False,
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='Notation',
            fields=[
                ('id', models.AutoField(serialize=False, auto_created=True, verbose_name='ID', primary_key=True)),
                ('title', models.CharField(null=True, max_length=150)),
                ('content', models.TextField(null=True)),
                ('time_stamp', models.DateTimeField(auto_now_add=True, default=datetime.datetime(2015, 7, 4, 15, 20, 9, 798316, tzinfo=utc))),
                ('link', models.URLField(blank=True, verbose_name='url_link')),
            ],
            options={
                'abstract': False,
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='Postgraduate',
            fields=[
                ('name', models.CharField(serialize=False, primary_key=True, verbose_name='姓名', max_length=150)),
                ('Email', models.EmailField(max_length=75)),
                ('mainpage', models.URLField(blank=True, verbose_name='个人主页')),
                ('grade', models.CharField(verbose_name='年级', max_length=1)),
                ('educational_level', models.CharField(verbose_name='学位（博士/硕士）', max_length=18)),
            ],
            options={
                'abstract': False,
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='Professor',
            fields=[
                ('name', models.CharField(serialize=False, primary_key=True, verbose_name='姓名', max_length=150)),
                ('Email', models.EmailField(max_length=75)),
                ('mainpage', models.URLField(blank=True, verbose_name='个人主页')),
                ('job_title', models.CharField(null=True, verbose_name='职称', max_length=150)),
            ],
            options={
                'abstract': False,
            },
            bases=(models.Model,),
        ),
    ]
