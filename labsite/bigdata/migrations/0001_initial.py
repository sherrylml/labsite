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
            name='Academic',
            fields=[
                ('id', models.AutoField(serialize=False, verbose_name='ID', auto_created=True, primary_key=True)),
                ('title', models.CharField(null=True, max_length=150)),
                ('content', models.TextField(null=True)),
                ('time_stamp', models.DateTimeField(auto_now_add=True, default=datetime.datetime(2015, 7, 12, 8, 50, 5, 805638, tzinfo=utc))),
                ('picture', models.ImageField(upload_to='academic', null=True, verbose_name='照片', blank=True)),
            ],
            options={
                'abstract': False,
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='Join1',
            fields=[
                ('id', models.AutoField(serialize=False, verbose_name='ID', auto_created=True, primary_key=True)),
                ('title', models.CharField(null=True, max_length=150)),
                ('content', models.TextField(null=True)),
                ('time_stamp', models.DateTimeField(auto_now_add=True, default=datetime.datetime(2015, 7, 12, 8, 50, 5, 805638, tzinfo=utc))),
            ],
            options={
                'abstract': False,
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='Join2',
            fields=[
                ('id', models.AutoField(serialize=False, verbose_name='ID', auto_created=True, primary_key=True)),
                ('title', models.CharField(null=True, max_length=150)),
                ('content', models.TextField(null=True)),
                ('time_stamp', models.DateTimeField(auto_now_add=True, default=datetime.datetime(2015, 7, 12, 8, 50, 5, 805638, tzinfo=utc))),
            ],
            options={
                'abstract': False,
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='Meetings',
            fields=[
                ('id', models.AutoField(serialize=False, verbose_name='ID', auto_created=True, primary_key=True)),
                ('title', models.CharField(null=True, max_length=150)),
                ('content', models.TextField(null=True)),
                ('time_stamp', models.DateTimeField(auto_now_add=True, default=datetime.datetime(2015, 7, 12, 8, 50, 5, 805638, tzinfo=utc))),
                ('link', models.URLField(verbose_name='url_link', blank=True)),
            ],
            options={
                'abstract': False,
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='News',
            fields=[
                ('id', models.AutoField(serialize=False, verbose_name='ID', auto_created=True, primary_key=True)),
                ('title', models.CharField(null=True, max_length=150)),
                ('content', models.TextField(null=True)),
                ('time_stamp', models.DateTimeField(auto_now_add=True, default=datetime.datetime(2015, 7, 12, 8, 50, 5, 805638, tzinfo=utc))),
                ('picture', models.ImageField(upload_to='news', null=True, verbose_name='照片', blank=True)),
            ],
            options={
                'abstract': False,
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='Notices',
            fields=[
                ('id', models.AutoField(serialize=False, verbose_name='ID', auto_created=True, primary_key=True)),
                ('title', models.CharField(null=True, max_length=150)),
                ('content', models.TextField(null=True)),
                ('time_stamp', models.DateTimeField(auto_now_add=True, default=datetime.datetime(2015, 7, 12, 8, 50, 5, 805638, tzinfo=utc))),
                ('picture', models.ImageField(upload_to='notices', null=True, verbose_name='照片', blank=True)),
            ],
            options={
                'abstract': False,
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='PatPri',
            fields=[
                ('id', models.AutoField(serialize=False, verbose_name='ID', auto_created=True, primary_key=True)),
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
                ('id', models.AutoField(serialize=False, verbose_name='ID', auto_created=True, primary_key=True)),
                ('name', models.CharField(max_length=150, verbose_name='姓名')),
                ('Email', models.EmailField(max_length=75, blank=True)),
                ('address', models.CharField(max_length=150, verbose_name='通信地址', blank=True)),
                ('postcode', models.CharField(max_length=6, verbose_name='邮政编码', default='000000')),
                ('edu_bg', models.TextField(verbose_name='教育背景', blank=True)),
                ('image', models.ImageField(upload_to='', null=True, verbose_name='个人照片', blank=True)),
                ('grade', models.CharField(choices=[(1, 1), (2, 2), (3, 3), (4, 4), (5, 5)], max_length=1, verbose_name='年级')),
                ('educational_level', models.CharField(choices=[('master', '硕士'), ('doctor', '博士')], max_length=18, verbose_name='学位（博士/硕士）')),
                ('patent_prizes', models.ManyToManyField(null=True, verbose_name='专利与奖励', blank=True, to='bigdata.PatPri')),
            ],
            options={
                'db_table': 'Postgraduate',
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='Professor',
            fields=[
                ('id', models.AutoField(serialize=False, verbose_name='ID', auto_created=True, primary_key=True)),
                ('name', models.CharField(max_length=150, verbose_name='姓名')),
                ('Email', models.EmailField(max_length=75, blank=True)),
                ('address', models.CharField(max_length=150, verbose_name='通信地址', blank=True)),
                ('postcode', models.CharField(max_length=6, verbose_name='邮政编码', default='000000')),
                ('edu_bg', models.TextField(verbose_name='教育背景', blank=True)),
                ('image', models.ImageField(upload_to='', null=True, verbose_name='个人照片', blank=True)),
                ('job_title', models.CharField(max_length=150, verbose_name='职称', blank=True)),
                ('patent_prizes', models.ManyToManyField(null=True, verbose_name='专利与奖励', blank=True, to='bigdata.PatPri')),
            ],
            options={
                'db_table': 'Professor',
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='PubInf',
            fields=[
                ('id', models.AutoField(serialize=False, verbose_name='ID', auto_created=True, primary_key=True)),
                ('publish_infor', models.TextField(verbose_name='出版信息')),
            ],
            options={
                'db_table': 'PubInf',
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='Relax',
            fields=[
                ('id', models.AutoField(serialize=False, verbose_name='ID', auto_created=True, primary_key=True)),
                ('title', models.CharField(null=True, max_length=150)),
                ('content', models.TextField(null=True)),
                ('time_stamp', models.DateTimeField(auto_now_add=True, default=datetime.datetime(2015, 7, 12, 8, 50, 5, 805638, tzinfo=utc))),
                ('picture', models.ImageField(upload_to='relax', null=True, verbose_name='照片', blank=True)),
            ],
            options={
                'abstract': False,
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='ResAct',
            fields=[
                ('id', models.AutoField(serialize=False, verbose_name='ID', auto_created=True, primary_key=True)),
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
                ('id', models.AutoField(serialize=False, verbose_name='ID', auto_created=True, primary_key=True)),
                ('research_direction', models.TextField(verbose_name='研究方向', blank=True)),
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
                ('id', models.AutoField(serialize=False, verbose_name='ID', auto_created=True, primary_key=True)),
                ('work_experience', models.TextField(verbose_name='工作经历', blank=True)),
            ],
            options={
                'db_table': 'WorkExp',
            },
            bases=(models.Model,),
        ),
        migrations.AddField(
            model_name='professor',
            name='publish_infors',
            field=models.ManyToManyField(null=True, verbose_name='出版信息', blank=True, to='bigdata.PubInf'),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='professor',
            name='research_activities',
            field=models.ManyToManyField(null=True, verbose_name='科研活动', blank=True, to='bigdata.ResAct'),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='professor',
            name='work_experiences',
            field=models.ManyToManyField(null=True, verbose_name='工作经历', blank=True, to='bigdata.WorkExp'),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='postgraduate',
            name='publish_infors',
            field=models.ManyToManyField(null=True, verbose_name='出版信息', blank=True, to='bigdata.PubInf'),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='postgraduate',
            name='research_activities',
            field=models.ManyToManyField(null=True, verbose_name='科研活动', blank=True, to='bigdata.ResAct'),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='postgraduate',
            name='work_experiences',
            field=models.ManyToManyField(null=True, verbose_name='工作经历', blank=True, to='bigdata.WorkExp'),
            preserve_default=True,
        ),
    ]
