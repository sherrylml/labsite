# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import datetime
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('bigdata', '0007_auto_20150712_2333'),
    ]

    operations = [
        migrations.CreateModel(
            name='PatPri1',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('patent_prize', models.TextField(blank=True, verbose_name='专利与奖励')),
                ('postgraduate', models.ForeignKey(to='bigdata.Postgraduate')),
            ],
            options={
                'db_table': 'PatPri1',
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='PubInf1',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('publish_infor', models.TextField(blank=True, verbose_name='出版信息')),
                ('postgraduate', models.ForeignKey(to='bigdata.Postgraduate')),
            ],
            options={
                'db_table': 'PubInf1',
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='ResAct1',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('research_activitiy', models.TextField(blank=True, verbose_name='科研活动')),
                ('postgraduate', models.ForeignKey(to='bigdata.Postgraduate')),
            ],
            options={
                'db_table': 'ResAct1',
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='ResDir1',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('research_direction', models.TextField(blank=True, verbose_name='研究方向')),
                ('postgraduate', models.ForeignKey(to='bigdata.Postgraduate')),
            ],
            options={
                'db_table': 'ResDir1',
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='WorkExp1',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('work_experience', models.TextField(blank=True, verbose_name='工作经历')),
                ('postgraduate', models.ForeignKey(to='bigdata.Postgraduate')),
            ],
            options={
                'db_table': 'WorkExp1',
            },
            bases=(models.Model,),
        ),
        migrations.RemoveField(
            model_name='patpri',
            name='postgraduate',
        ),
        migrations.RemoveField(
            model_name='postgraduate',
            name='mainpage',
        ),
        migrations.RemoveField(
            model_name='professor',
            name='mainpage',
        ),
        migrations.RemoveField(
            model_name='pubinf',
            name='postgraduate',
        ),
        migrations.RemoveField(
            model_name='resact',
            name='postgraduate',
        ),
        migrations.RemoveField(
            model_name='resdir',
            name='postgraduate',
        ),
        migrations.RemoveField(
            model_name='workexp',
            name='postgraduate',
        ),
        migrations.AlterField(
            model_name='academic',
            name='time_stamp',
            field=models.DateTimeField(auto_now_add=True, default=datetime.datetime(2015, 7, 12, 16, 24, 0, 704643, tzinfo=utc)),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='join1',
            name='time_stamp',
            field=models.DateTimeField(auto_now_add=True, default=datetime.datetime(2015, 7, 12, 16, 24, 0, 704643, tzinfo=utc)),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='join2',
            name='time_stamp',
            field=models.DateTimeField(auto_now_add=True, default=datetime.datetime(2015, 7, 12, 16, 24, 0, 704643, tzinfo=utc)),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='meetings',
            name='time_stamp',
            field=models.DateTimeField(auto_now_add=True, default=datetime.datetime(2015, 7, 12, 16, 24, 0, 704643, tzinfo=utc)),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='news',
            name='time_stamp',
            field=models.DateTimeField(auto_now_add=True, default=datetime.datetime(2015, 7, 12, 16, 24, 0, 704643, tzinfo=utc)),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='notices',
            name='time_stamp',
            field=models.DateTimeField(auto_now_add=True, default=datetime.datetime(2015, 7, 12, 16, 24, 0, 704643, tzinfo=utc)),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='patpri',
            name='patent_prize',
            field=models.TextField(blank=True, verbose_name='专利与奖励'),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='postgraduate',
            name='grade',
            field=models.CharField(verbose_name='年级', choices=[(1, 1), (2, 2), (3, 3), (4, 4), (5, 5)], max_length=2),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='pubinf',
            name='publish_infor',
            field=models.TextField(blank=True, verbose_name='出版信息'),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='relax',
            name='time_stamp',
            field=models.DateTimeField(auto_now_add=True, default=datetime.datetime(2015, 7, 12, 16, 24, 0, 704643, tzinfo=utc)),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='resact',
            name='research_activitiy',
            field=models.TextField(blank=True, verbose_name='科研活动'),
            preserve_default=True,
        ),
    ]
