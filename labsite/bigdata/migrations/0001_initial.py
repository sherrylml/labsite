# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import datetime
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='News',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False, verbose_name='ID', auto_created=True)),
                ('title', models.CharField(max_length=150, null=True)),
                ('content', models.TextField(null=True)),
                ('time_stamp', models.DateTimeField(auto_now_add=True, default=datetime.datetime(2015, 7, 6, 8, 49, 31, 571717, tzinfo=utc))),
                ('link', models.URLField(blank=True, verbose_name='url_link')),
            ],
            options={
                'abstract': False,
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='PatPri',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False, verbose_name='ID', auto_created=True)),
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
                ('id', models.AutoField(primary_key=True, serialize=False, verbose_name='ID', auto_created=True)),
                ('name', models.CharField(max_length=150, verbose_name='姓名')),
                ('Email', models.EmailField(max_length=75, blank=True)),
                ('mainpage', models.URLField(blank=True, verbose_name='个人主页')),
                ('address', models.CharField(max_length=150, blank=True, verbose_name='通信地址')),
                ('postcode', models.CharField(max_length=6, verbose_name='邮政编码', default='000000')),
                ('edu_bg', models.TextField(blank=True, verbose_name='教育背景')),
                ('image', models.ImageField(blank=True, upload_to='', null=True, verbose_name='个人照片')),
                ('grade', models.CharField(max_length=1, verbose_name='年级', choices=[(1, 1), (2, 2), (3, 3), (4, 4), (5, 5)])),
                ('educational_level', models.CharField(max_length=18, verbose_name='学位（博士/硕士）', choices=[('master', '硕士'), ('doctor', '博士')])),
                ('patent_prizes', models.ManyToManyField(blank=True, null=True, to='bigdata.PatPri', verbose_name='专利与奖励')),
            ],
            options={
                'db_table': 'Postgraduate',
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='Professor',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False, verbose_name='ID', auto_created=True)),
                ('name', models.CharField(max_length=150, verbose_name='姓名')),
                ('Email', models.EmailField(max_length=75, blank=True)),
                ('mainpage', models.URLField(blank=True, verbose_name='个人主页')),
                ('address', models.CharField(max_length=150, blank=True, verbose_name='通信地址')),
                ('postcode', models.CharField(max_length=6, verbose_name='邮政编码', default='000000')),
                ('edu_bg', models.TextField(blank=True, verbose_name='教育背景')),
                ('image', models.ImageField(blank=True, upload_to='', null=True, verbose_name='个人照片')),
                ('job_title', models.CharField(max_length=150, blank=True, verbose_name='职称')),
                ('patent_prizes', models.ManyToManyField(blank=True, null=True, to='bigdata.PatPri', verbose_name='专利与奖励')),
            ],
            options={
                'db_table': 'Professor',
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='PubInf',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False, verbose_name='ID', auto_created=True)),
                ('publish_infor', models.TextField(verbose_name='出版信息')),
            ],
            options={
                'db_table': 'PubInf',
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='ResAct',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False, verbose_name='ID', auto_created=True)),
                ('research_activitiy', models.TextField(verbose_name='科研活动')),
            ],
            options={
                'db_table': 'ResAct',
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='ResDir',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False, verbose_name='ID', auto_created=True)),
                ('research_direction', models.TextField(blank=True, verbose_name='研究方向')),
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
                ('id', models.AutoField(primary_key=True, serialize=False, verbose_name='ID', auto_created=True)),
                ('work_experience', models.TextField(blank=True, verbose_name='工作经历')),
            ],
            options={
                'db_table': 'WorkExp',
            },
            bases=(models.Model,),
        ),
        migrations.AddField(
            model_name='professor',
            name='publish_infors',
            field=models.ManyToManyField(blank=True, null=True, to='bigdata.PubInf', verbose_name='出版信息'),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='professor',
            name='research_activities',
            field=models.ManyToManyField(blank=True, null=True, to='bigdata.ResAct', verbose_name='科研活动'),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='professor',
            name='work_experiences',
            field=models.ManyToManyField(blank=True, null=True, to='bigdata.WorkExp', verbose_name='工作经历'),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='postgraduate',
            name='publish_infors',
            field=models.ManyToManyField(blank=True, null=True, to='bigdata.PubInf', verbose_name='出版信息'),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='postgraduate',
            name='research_activities',
            field=models.ManyToManyField(blank=True, null=True, to='bigdata.ResAct', verbose_name='科研活动'),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='postgraduate',
            name='work_experiences',
            field=models.ManyToManyField(blank=True, null=True, to='bigdata.WorkExp', verbose_name='工作经历'),
            preserve_default=True,
        ),
    ]
