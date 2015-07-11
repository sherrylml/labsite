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
                ('id', models.AutoField(serialize=False, auto_created=True, verbose_name='ID', primary_key=True)),
                ('title', models.CharField(max_length=150, null=True)),
                ('content', models.TextField(null=True)),
                ('time_stamp', models.DateTimeField(auto_now_add=True, default=datetime.datetime(2015, 7, 10, 5, 39, 21, 280482, tzinfo=utc))),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='Postgraduate',
            fields=[
                ('id', models.AutoField(serialize=False, auto_created=True, verbose_name='ID', primary_key=True)),
                ('name', models.CharField(max_length=150, verbose_name='姓名')),
                ('Email', models.EmailField(blank=True, max_length=75)),
                ('mainpage', models.URLField(blank=True, verbose_name='个人主页')),
                ('address', models.CharField(blank=True, max_length=150, verbose_name='通信地址')),
                ('postcode', models.CharField(default='000000', max_length=6, verbose_name='邮政编码')),
                ('edu_bg', models.TextField(blank=True, verbose_name='教育背景')),
                ('image', models.ImageField(upload_to='', verbose_name='个人照片', null=True)),
                ('research_direction', models.TextField(blank=True, verbose_name='研究方向')),
                ('work_experience', models.TextField(blank=True, verbose_name='工作经历')),
                ('patent_prize', models.TextField(blank=True, verbose_name='专利与奖励')),
                ('publish_infor', models.TextField(blank=True, verbose_name='出版信息')),
                ('research_activities', models.TextField(blank=True, verbose_name='科研活动')),
                ('grade', models.CharField(max_length=1, verbose_name='年级', choices=[(1, 1), (2, 2), (3, 3), (4, 4), (5, 5)])),
                ('educational_level', models.CharField(max_length=18, verbose_name='学位（博士/硕士）', choices=[('master', '硕士'), ('doctor', '博士')])),
            ],
            options={
                'abstract': False,
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='Professor',
            fields=[
                ('id', models.AutoField(serialize=False, auto_created=True, verbose_name='ID', primary_key=True)),
                ('name', models.CharField(max_length=150, verbose_name='姓名')),
                ('Email', models.EmailField(blank=True, max_length=75)),
                ('mainpage', models.URLField(blank=True, verbose_name='个人主页')),
                ('address', models.CharField(blank=True, max_length=150, verbose_name='通信地址')),
                ('postcode', models.CharField(default='000000', max_length=6, verbose_name='邮政编码')),
                ('edu_bg', models.TextField(blank=True, verbose_name='教育背景')),
                ('image', models.ImageField(upload_to='', verbose_name='个人照片', null=True)),
                ('research_direction', models.TextField(blank=True, verbose_name='研究方向')),
                ('work_experience', models.TextField(blank=True, verbose_name='工作经历')),
                ('patent_prize', models.TextField(blank=True, verbose_name='专利与奖励')),
                ('publish_infor', models.TextField(blank=True, verbose_name='出版信息')),
                ('research_activities', models.TextField(blank=True, verbose_name='科研活动')),
                ('job_title', models.CharField(max_length=150, verbose_name='职称', null=True)),
            ],
            options={
                'abstract': False,
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='Publisher',
            fields=[
                ('id', models.AutoField(serialize=False, auto_created=True, verbose_name='ID', primary_key=True)),
                ('name', models.CharField(max_length=25)),
                ('address', models.CharField(max_length=30)),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.AddField(
            model_name='professor',
            name='publisher',
            field=models.ForeignKey(to='bigdata.Publisher'),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='postgraduate',
            name='publisher',
            field=models.ForeignKey(to='bigdata.Publisher'),
            preserve_default=True,
        ),
    ]
