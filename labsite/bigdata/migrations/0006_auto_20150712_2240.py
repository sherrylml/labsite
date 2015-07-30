# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
from django.utils.timezone import utc
import datetime


class Migration(migrations.Migration):

    dependencies = [
        ('bigdata', '0005_auto_20150712_2221'),
    ]

    operations = [
        migrations.CreateModel(
            name='PatPri',
            fields=[
                ('id', models.AutoField(primary_key=True, auto_created=True, verbose_name='ID', serialize=False)),
                ('patent_prize', models.TextField(verbose_name='专利与奖励')),
            ],
            options={
                'db_table': 'PatPri',
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='Postgraduate',
            fields=[
                ('id', models.AutoField(primary_key=True, auto_created=True, verbose_name='ID', serialize=False)),
                ('name', models.CharField(max_length=150, verbose_name='姓名')),
                ('Email', models.EmailField(blank=True, max_length=75)),
                ('mainpage', models.URLField(blank=True, verbose_name='个人主页')),
                ('address', models.CharField(blank=True, max_length=150, verbose_name='通信地址')),
                ('postcode', models.CharField(default='000000', max_length=6, verbose_name='邮政编码')),
                ('edu_bg', models.TextField(blank=True, verbose_name='教育背景')),
                ('image', models.ImageField(blank=True, upload_to='', verbose_name='个人照片', null=True)),
                ('grade', models.CharField(choices=[(1, 1), (2, 2), (3, 3), (4, 4), (5, 5)], max_length=1, verbose_name='年级')),
                ('educational_level', models.CharField(choices=[('master', '硕士'), ('doctor', '博士')], max_length=18, verbose_name='学位（博士/硕士）')),
            ],
            options={
                'db_table': 'Postgraduate',
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='Professor',
            fields=[
                ('id', models.AutoField(primary_key=True, auto_created=True, verbose_name='ID', serialize=False)),
                ('name', models.CharField(max_length=150, verbose_name='姓名')),
                ('Email', models.EmailField(blank=True, max_length=75)),
                ('mainpage', models.URLField(blank=True, verbose_name='个人主页')),
                ('address', models.CharField(blank=True, max_length=150, verbose_name='通信地址')),
                ('postcode', models.CharField(default='000000', max_length=6, verbose_name='邮政编码')),
                ('edu_bg', models.TextField(blank=True, verbose_name='教育背景')),
                ('image', models.ImageField(blank=True, upload_to='', verbose_name='个人照片', null=True)),
                ('job_title', models.CharField(blank=True, max_length=150, verbose_name='职称')),
            ],
            options={
                'db_table': 'Professor',
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='PubInf',
            fields=[
                ('id', models.AutoField(primary_key=True, auto_created=True, verbose_name='ID', serialize=False)),
                ('publish_infor', models.TextField(verbose_name='出版信息')),
                ('postgraduate', models.ForeignKey(to='bigdata.Postgraduate')),
                ('professor', models.ForeignKey(to='bigdata.Professor')),
            ],
            options={
                'db_table': 'PubInf',
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='ResAct',
            fields=[
                ('id', models.AutoField(primary_key=True, auto_created=True, verbose_name='ID', serialize=False)),
                ('research_activitiy', models.TextField(verbose_name='科研活动')),
                ('postgraduate', models.ForeignKey(to='bigdata.Postgraduate')),
                ('professor', models.ForeignKey(to='bigdata.Professor')),
            ],
            options={
                'db_table': 'ResAct',
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='ResDir',
            fields=[
                ('id', models.AutoField(primary_key=True, auto_created=True, verbose_name='ID', serialize=False)),
                ('research_direction', models.TextField(blank=True, verbose_name='研究方向')),
                ('postgraduate', models.ForeignKey(to='bigdata.Postgraduate')),
                ('professor', models.ForeignKey(to='bigdata.Professor')),
            ],
            options={
                'db_table': 'ResDir',
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='WorkExp',
            fields=[
                ('id', models.AutoField(primary_key=True, auto_created=True, verbose_name='ID', serialize=False)),
                ('work_experience', models.TextField(blank=True, verbose_name='工作经历')),
                ('postgraduate', models.ForeignKey(to='bigdata.Postgraduate')),
                ('professor', models.ForeignKey(to='bigdata.Professor')),
            ],
            options={
                'db_table': 'WorkExp',
            },
            bases=(models.Model,),
        ),
        migrations.AddField(
            model_name='patpri',
            name='postgraduate',
            field=models.ForeignKey(to='bigdata.Postgraduate'),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='patpri',
            name='professor',
            field=models.ForeignKey(to='bigdata.Professor'),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='academic',
            name='time_stamp',
            field=models.DateTimeField(default=datetime.datetime(2015, 7, 12, 14, 40, 1, 711666, tzinfo=utc), auto_now_add=True),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='join1',
            name='time_stamp',
            field=models.DateTimeField(default=datetime.datetime(2015, 7, 12, 14, 40, 1, 711666, tzinfo=utc), auto_now_add=True),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='join2',
            name='time_stamp',
            field=models.DateTimeField(default=datetime.datetime(2015, 7, 12, 14, 40, 1, 711666, tzinfo=utc), auto_now_add=True),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='meetings',
            name='time_stamp',
            field=models.DateTimeField(default=datetime.datetime(2015, 7, 12, 14, 40, 1, 711666, tzinfo=utc), auto_now_add=True),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='news',
            name='time_stamp',
            field=models.DateTimeField(default=datetime.datetime(2015, 7, 12, 14, 40, 1, 711666, tzinfo=utc), auto_now_add=True),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='notices',
            name='time_stamp',
            field=models.DateTimeField(default=datetime.datetime(2015, 7, 12, 14, 40, 1, 711666, tzinfo=utc), auto_now_add=True),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='relax',
            name='time_stamp',
            field=models.DateTimeField(default=datetime.datetime(2015, 7, 12, 14, 40, 1, 711666, tzinfo=utc), auto_now_add=True),
            preserve_default=True,
        ),
    ]
