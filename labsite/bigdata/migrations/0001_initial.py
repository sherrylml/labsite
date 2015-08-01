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
                ('id', models.AutoField(auto_created=True, verbose_name='ID', serialize=False, primary_key=True)),
                ('title', models.CharField(null=True, max_length=150)),
                ('content', models.TextField(null=True)),
                ('time_stamp', models.DateTimeField(auto_now_add=True, default=datetime.datetime(2015, 7, 31, 14, 6, 53, 134264, tzinfo=utc))),
                ('picture', models.ImageField(blank=True, null=True, verbose_name='照片', upload_to='academic')),
            ],
            options={
                'verbose_name': '学术交流活动',
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='Directions',
            fields=[
                ('id', models.AutoField(auto_created=True, verbose_name='ID', serialize=False, primary_key=True)),
                ('research_direction', models.TextField(blank=True, verbose_name='研究方向')),
            ],
            options={
                'db_table': 'Directions',
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='Images',
            fields=[
                ('id', models.AutoField(auto_created=True, verbose_name='ID', serialize=False, primary_key=True)),
                ('images', models.ImageField(blank=True, upload_to='', verbose_name='图片')),
                ('directions', models.ForeignKey(to='bigdata.Directions')),
            ],
            options={
                'db_table': 'Images',
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='Join1',
            fields=[
                ('id', models.AutoField(auto_created=True, verbose_name='ID', serialize=False, primary_key=True)),
                ('title', models.CharField(null=True, max_length=150)),
                ('content', models.TextField(null=True)),
                ('time_stamp', models.DateTimeField(auto_now_add=True, default=datetime.datetime(2015, 7, 31, 14, 6, 53, 134264, tzinfo=utc))),
            ],
            options={
                'verbose_name': '招生信息',
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='Join2',
            fields=[
                ('id', models.AutoField(auto_created=True, verbose_name='ID', serialize=False, primary_key=True)),
                ('title', models.CharField(null=True, max_length=150)),
                ('content', models.TextField(null=True)),
                ('time_stamp', models.DateTimeField(auto_now_add=True, default=datetime.datetime(2015, 7, 31, 14, 6, 53, 134264, tzinfo=utc))),
            ],
            options={
                'verbose_name': '人才招聘',
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='Lab',
            fields=[
                ('id', models.AutoField(auto_created=True, verbose_name='ID', serialize=False, primary_key=True)),
                ('introduction', models.TextField(null=True)),
                ('direction', models.TextField(null=True)),
                ('achievement', models.TextField(null=True)),
            ],
            options={
                'verbose_name': '实验室相关信息',
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='Meetings',
            fields=[
                ('id', models.AutoField(auto_created=True, verbose_name='ID', serialize=False, primary_key=True)),
                ('title', models.CharField(null=True, max_length=150)),
                ('content', models.TextField(null=True)),
                ('time_stamp', models.DateTimeField(auto_now_add=True, default=datetime.datetime(2015, 7, 31, 14, 6, 53, 134264, tzinfo=utc))),
                ('link', models.URLField(blank=True, verbose_name='url_link')),
            ],
            options={
                'verbose_name': '近期学术会议',
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='News',
            fields=[
                ('id', models.AutoField(auto_created=True, verbose_name='ID', serialize=False, primary_key=True)),
                ('title', models.CharField(null=True, max_length=150)),
                ('content', models.TextField(null=True)),
                ('time_stamp', models.DateTimeField(auto_now_add=True, default=datetime.datetime(2015, 7, 31, 14, 6, 53, 134264, tzinfo=utc))),
                ('picture', models.ImageField(blank=True, null=True, verbose_name='照片', upload_to='news')),
            ],
            options={
                'verbose_name': '新闻动态',
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='Notices',
            fields=[
                ('id', models.AutoField(auto_created=True, verbose_name='ID', serialize=False, primary_key=True)),
                ('title', models.CharField(null=True, max_length=150)),
                ('content', models.TextField(null=True)),
                ('time_stamp', models.DateTimeField(auto_now_add=True, default=datetime.datetime(2015, 7, 31, 14, 6, 53, 134264, tzinfo=utc))),
                ('picture', models.ImageField(blank=True, null=True, verbose_name='照片', upload_to='notices')),
            ],
            options={
                'verbose_name': '通知公告',
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='PatPri',
            fields=[
                ('id', models.AutoField(auto_created=True, verbose_name='ID', serialize=False, primary_key=True)),
                ('patent_prize', models.TextField(blank=True, verbose_name='专利与奖励')),
            ],
            options={
                'db_table': 'PatPri',
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='PatPri1',
            fields=[
                ('id', models.AutoField(auto_created=True, verbose_name='ID', serialize=False, primary_key=True)),
                ('patent_prize', models.TextField(blank=True, verbose_name='专利与奖励')),
            ],
            options={
                'db_table': 'PatPri1',
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='Postgraduate',
            fields=[
                ('id', models.AutoField(auto_created=True, verbose_name='ID', serialize=False, primary_key=True)),
                ('name', models.CharField(verbose_name='姓名', max_length=150)),
                ('Email', models.EmailField(blank=True, max_length=75)),
                ('address', models.CharField(blank=True, verbose_name='通信地址', max_length=150)),
                ('postcode', models.CharField(verbose_name='邮政编码', max_length=6, default='000000')),
                ('edu_bg', models.TextField(blank=True, verbose_name='教育背景')),
                ('image', models.ImageField(blank=True, null=True, verbose_name='个人照片', upload_to='memberImg')),
                ('grade', models.CharField(choices=[('1', 1), ('2', 2), ('3', 3), ('4', 4), ('5', 5)], verbose_name='年级', max_length=2)),
                ('educational_level', models.CharField(choices=[('master', '硕士'), ('doctor', '博士')], verbose_name='学位（博士/硕士）', max_length=18)),
            ],
            options={
                'verbose_name': '学生信息',
                'db_table': 'Postgraduate',
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='Professor',
            fields=[
                ('id', models.AutoField(auto_created=True, verbose_name='ID', serialize=False, primary_key=True)),
                ('name', models.CharField(verbose_name='姓名', max_length=150)),
                ('Email', models.EmailField(blank=True, max_length=75)),
                ('address', models.CharField(blank=True, verbose_name='通信地址', max_length=150)),
                ('postcode', models.CharField(verbose_name='邮政编码', max_length=6, default='000000')),
                ('edu_bg', models.TextField(blank=True, verbose_name='教育背景')),
                ('image', models.ImageField(blank=True, null=True, verbose_name='个人照片', upload_to='memberImg')),
                ('job_title', models.CharField(blank=True, verbose_name='职称', max_length=150)),
            ],
            options={
                'verbose_name': '老师信息',
                'db_table': 'Professor',
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='PubInf',
            fields=[
                ('id', models.AutoField(auto_created=True, verbose_name='ID', serialize=False, primary_key=True)),
                ('publish_info', models.TextField(blank=True, verbose_name='出版信息')),
                ('professor', models.ForeignKey(to='bigdata.Professor')),
            ],
            options={
                'db_table': 'PubInf',
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='PubInf1',
            fields=[
                ('id', models.AutoField(auto_created=True, verbose_name='ID', serialize=False, primary_key=True)),
                ('publish_infor', models.TextField(blank=True, verbose_name='出版信息')),
                ('postgraduate', models.ForeignKey(to='bigdata.Postgraduate')),
            ],
            options={
                'db_table': 'PubInf1',
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='Relax',
            fields=[
                ('id', models.AutoField(auto_created=True, verbose_name='ID', serialize=False, primary_key=True)),
                ('title', models.CharField(null=True, max_length=150)),
                ('content', models.TextField(null=True)),
                ('time_stamp', models.DateTimeField(auto_now_add=True, default=datetime.datetime(2015, 7, 31, 14, 6, 53, 134264, tzinfo=utc))),
                ('picture', models.ImageField(blank=True, null=True, verbose_name='照片', upload_to='relax')),
            ],
            options={
                'verbose_name': '休闲活动',
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='ResAct',
            fields=[
                ('id', models.AutoField(auto_created=True, verbose_name='ID', serialize=False, primary_key=True)),
                ('research_activity', models.TextField(blank=True, verbose_name='科研活动')),
                ('professor', models.ForeignKey(to='bigdata.Professor')),
            ],
            options={
                'db_table': 'ResAct',
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='ResAct1',
            fields=[
                ('id', models.AutoField(auto_created=True, verbose_name='ID', serialize=False, primary_key=True)),
                ('research_activitiy', models.TextField(blank=True, verbose_name='科研活动')),
                ('postgraduate', models.ForeignKey(to='bigdata.Postgraduate')),
            ],
            options={
                'db_table': 'ResAct1',
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='ResDir',
            fields=[
                ('id', models.AutoField(auto_created=True, verbose_name='ID', serialize=False, primary_key=True)),
                ('research_direction', models.TextField(blank=True, verbose_name='研究方向')),
                ('professor', models.ForeignKey(to='bigdata.Professor')),
            ],
            options={
                'db_table': 'ResDir',
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='ResDir1',
            fields=[
                ('id', models.AutoField(auto_created=True, verbose_name='ID', serialize=False, primary_key=True)),
                ('research_direction', models.TextField(blank=True, verbose_name='研究方向')),
                ('postgraduate', models.ForeignKey(to='bigdata.Postgraduate')),
            ],
            options={
                'db_table': 'ResDir1',
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='WorkExp',
            fields=[
                ('id', models.AutoField(auto_created=True, verbose_name='ID', serialize=False, primary_key=True)),
                ('work_experience', models.TextField(blank=True, verbose_name='工作经历')),
                ('professor', models.ForeignKey(to='bigdata.Professor')),
            ],
            options={
                'db_table': 'WorkExp',
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='WorkExp1',
            fields=[
                ('id', models.AutoField(auto_created=True, verbose_name='ID', serialize=False, primary_key=True)),
                ('work_experience', models.TextField(blank=True, verbose_name='工作经历')),
                ('postgraduate', models.ForeignKey(to='bigdata.Postgraduate')),
            ],
            options={
                'db_table': 'WorkExp1',
            },
            bases=(models.Model,),
        ),
        migrations.AddField(
            model_name='patpri1',
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
        migrations.AddField(
            model_name='images',
            name='lab',
            field=models.ForeignKey(to='bigdata.Lab'),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='directions',
            name='lab',
            field=models.ForeignKey(to='bigdata.Lab'),
            preserve_default=True,
        ),
    ]
