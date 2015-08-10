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
                ('id', models.AutoField(verbose_name='ID', primary_key=True, auto_created=True, serialize=False)),
                ('title', models.CharField(null=True, max_length=150)),
                ('content', models.TextField(null=True)),
                ('time_stamp', models.DateTimeField(default=datetime.datetime(2015, 8, 7, 7, 9, 11, 281727, tzinfo=utc), auto_now_add=True)),
                ('picture', models.ImageField(blank=True, verbose_name='照片', null=True, upload_to='academic')),
            ],
            options={
                'verbose_name': '学术交流活动',
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='AcademicEn',
            fields=[
                ('id', models.AutoField(verbose_name='ID', primary_key=True, auto_created=True, serialize=False)),
                ('title', models.CharField(null=True, max_length=150)),
                ('content', models.TextField(null=True)),
                ('time_stamp', models.DateTimeField(default=datetime.datetime(2015, 8, 7, 7, 9, 11, 293738, tzinfo=utc), auto_now_add=True)),
                ('picture', models.ImageField(blank=True, verbose_name='照片', null=True, upload_to='academic')),
            ],
            options={
                'verbose_name': '学术交流活动',
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='Directions',
            fields=[
                ('id', models.AutoField(verbose_name='ID', primary_key=True, auto_created=True, serialize=False)),
                ('research_direction', models.TextField(blank=True, verbose_name='研究方向')),
            ],
            options={
                'db_table': 'Directions',
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='DirectionsEn',
            fields=[
                ('id', models.AutoField(verbose_name='ID', primary_key=True, auto_created=True, serialize=False)),
                ('research_direction', models.TextField(blank=True, verbose_name='研究方向')),
            ],
            options={
                'db_table': 'DirectionsEn',
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='Images',
            fields=[
                ('id', models.AutoField(verbose_name='ID', primary_key=True, auto_created=True, serialize=False)),
                ('images', models.ImageField(blank=True, verbose_name='图片', null=True, upload_to='research_direction')),
                ('directions', models.ForeignKey(to='bigdata.Directions')),
            ],
            options={
                'db_table': 'Images',
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='ImagesEn',
            fields=[
                ('id', models.AutoField(verbose_name='ID', primary_key=True, auto_created=True, serialize=False)),
                ('images', models.ImageField(blank=True, verbose_name='图片', null=True, upload_to='research_direction')),
                ('directions', models.ForeignKey(to='bigdata.DirectionsEn')),
            ],
            options={
                'db_table': 'ImagesEn',
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='Join1',
            fields=[
                ('id', models.AutoField(verbose_name='ID', primary_key=True, auto_created=True, serialize=False)),
                ('title', models.CharField(null=True, max_length=150)),
                ('content', models.TextField(null=True)),
                ('time_stamp', models.DateTimeField(default=datetime.datetime(2015, 8, 7, 7, 9, 11, 281727, tzinfo=utc), auto_now_add=True)),
            ],
            options={
                'verbose_name': '招生信息',
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='Join1En',
            fields=[
                ('id', models.AutoField(verbose_name='ID', primary_key=True, auto_created=True, serialize=False)),
                ('title', models.CharField(null=True, max_length=150)),
                ('content', models.TextField(null=True)),
                ('time_stamp', models.DateTimeField(default=datetime.datetime(2015, 8, 7, 7, 9, 11, 293738, tzinfo=utc), auto_now_add=True)),
            ],
            options={
                'verbose_name': '招生信息',
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='Join2',
            fields=[
                ('id', models.AutoField(verbose_name='ID', primary_key=True, auto_created=True, serialize=False)),
                ('title', models.CharField(null=True, max_length=150)),
                ('content', models.TextField(null=True)),
                ('time_stamp', models.DateTimeField(default=datetime.datetime(2015, 8, 7, 7, 9, 11, 281727, tzinfo=utc), auto_now_add=True)),
            ],
            options={
                'verbose_name': '人才招聘',
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='Join2En',
            fields=[
                ('id', models.AutoField(verbose_name='ID', primary_key=True, auto_created=True, serialize=False)),
                ('title', models.CharField(null=True, max_length=150)),
                ('content', models.TextField(null=True)),
                ('time_stamp', models.DateTimeField(default=datetime.datetime(2015, 8, 7, 7, 9, 11, 293738, tzinfo=utc), auto_now_add=True)),
            ],
            options={
                'verbose_name': '人才招聘',
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='Lab',
            fields=[
                ('id', models.AutoField(verbose_name='ID', primary_key=True, auto_created=True, serialize=False)),
                ('introduction', models.TextField(null=True)),
                ('achievement', models.TextField(null=True)),
            ],
            options={
                'verbose_name': '研究组相关信息',
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='LabEn',
            fields=[
                ('id', models.AutoField(verbose_name='ID', primary_key=True, auto_created=True, serialize=False)),
                ('introduction', models.TextField(null=True)),
                ('achievement', models.TextField(null=True)),
            ],
            options={
                'verbose_name': '研究组相关信息',
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='Meetings',
            fields=[
                ('id', models.AutoField(verbose_name='ID', primary_key=True, auto_created=True, serialize=False)),
                ('title', models.CharField(null=True, max_length=150)),
                ('content', models.TextField(null=True)),
                ('time_stamp', models.DateTimeField(default=datetime.datetime(2015, 8, 7, 7, 9, 11, 281727, tzinfo=utc), auto_now_add=True)),
                ('link', models.URLField(blank=True, verbose_name='url_link')),
            ],
            options={
                'verbose_name': '近期学术会议',
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='MeetingsEn',
            fields=[
                ('id', models.AutoField(verbose_name='ID', primary_key=True, auto_created=True, serialize=False)),
                ('title', models.CharField(null=True, max_length=150)),
                ('content', models.TextField(null=True)),
                ('time_stamp', models.DateTimeField(default=datetime.datetime(2015, 8, 7, 7, 9, 11, 293738, tzinfo=utc), auto_now_add=True)),
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
                ('id', models.AutoField(verbose_name='ID', primary_key=True, auto_created=True, serialize=False)),
                ('title', models.CharField(null=True, max_length=150)),
                ('content', models.TextField(null=True)),
                ('time_stamp', models.DateTimeField(default=datetime.datetime(2015, 8, 7, 7, 9, 11, 281727, tzinfo=utc), auto_now_add=True)),
                ('picture', models.ImageField(blank=True, verbose_name='照片', null=True, upload_to='news')),
            ],
            options={
                'verbose_name': '新闻动态',
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='NewsEn',
            fields=[
                ('id', models.AutoField(verbose_name='ID', primary_key=True, auto_created=True, serialize=False)),
                ('title', models.CharField(null=True, max_length=150)),
                ('content', models.TextField(null=True)),
                ('time_stamp', models.DateTimeField(default=datetime.datetime(2015, 8, 7, 7, 9, 11, 293738, tzinfo=utc), auto_now_add=True)),
                ('picture', models.ImageField(blank=True, verbose_name='照片', null=True, upload_to='news')),
            ],
            options={
                'verbose_name': '新闻动态',
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='Notices',
            fields=[
                ('id', models.AutoField(verbose_name='ID', primary_key=True, auto_created=True, serialize=False)),
                ('title', models.CharField(null=True, max_length=150)),
                ('content', models.TextField(null=True)),
                ('time_stamp', models.DateTimeField(default=datetime.datetime(2015, 8, 7, 7, 9, 11, 281727, tzinfo=utc), auto_now_add=True)),
                ('picture', models.ImageField(blank=True, verbose_name='照片', null=True, upload_to='notices')),
            ],
            options={
                'verbose_name': '通知公告',
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='NoticesEn',
            fields=[
                ('id', models.AutoField(verbose_name='ID', primary_key=True, auto_created=True, serialize=False)),
                ('title', models.CharField(null=True, max_length=150)),
                ('content', models.TextField(null=True)),
                ('time_stamp', models.DateTimeField(default=datetime.datetime(2015, 8, 7, 7, 9, 11, 293738, tzinfo=utc), auto_now_add=True)),
                ('picture', models.ImageField(blank=True, verbose_name='照片', null=True, upload_to='notices')),
            ],
            options={
                'verbose_name': '通知公告',
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='PatPri',
            fields=[
                ('id', models.AutoField(verbose_name='ID', primary_key=True, auto_created=True, serialize=False)),
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
                ('id', models.AutoField(verbose_name='ID', primary_key=True, auto_created=True, serialize=False)),
                ('patent_prize', models.TextField(blank=True, verbose_name='专利与奖励')),
            ],
            options={
                'db_table': 'PatPri1',
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='PatPri1En',
            fields=[
                ('id', models.AutoField(verbose_name='ID', primary_key=True, auto_created=True, serialize=False)),
                ('patent_prize', models.TextField(blank=True, verbose_name='专利与奖励')),
            ],
            options={
                'db_table': 'PatPri1En',
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='PatPriEn',
            fields=[
                ('id', models.AutoField(verbose_name='ID', primary_key=True, auto_created=True, serialize=False)),
                ('patent_prize', models.TextField(blank=True, verbose_name='专利与奖励')),
            ],
            options={
                'db_table': 'PatPriEn',
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='Postgraduate',
            fields=[
                ('id', models.AutoField(verbose_name='ID', primary_key=True, auto_created=True, serialize=False)),
                ('name', models.CharField(verbose_name='name', max_length=150)),
                ('Email', models.EmailField(blank=True, max_length=75)),
                ('address', models.CharField(blank=True, verbose_name='address', max_length=150)),
                ('postcode', models.CharField(verbose_name='postcode', default='000000', max_length=6)),
                ('edu_bg', models.TextField(blank=True, verbose_name='educational_background')),
                ('image', models.ImageField(blank=True, verbose_name='photo', null=True, upload_to='memberImg')),
                ('grade', models.CharField(verbose_name='年级', choices=[('1', 1), ('2', 2), ('3', 3), ('4', 4), ('5', 5)], max_length=2)),
                ('educational_level', models.CharField(verbose_name='学位（博士/硕士）', choices=[('master', '硕士'), ('doctor', '博士')], max_length=18)),
            ],
            options={
                'verbose_name': '学生信息',
                'db_table': 'Postgraduate',
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='PostgraduateEn',
            fields=[
                ('id', models.AutoField(verbose_name='ID', primary_key=True, auto_created=True, serialize=False)),
                ('name', models.CharField(verbose_name='name', max_length=150)),
                ('Email', models.EmailField(blank=True, max_length=75)),
                ('address', models.CharField(blank=True, verbose_name='address', max_length=150)),
                ('postcode', models.CharField(verbose_name='postcode', default='000000', max_length=6)),
                ('edu_bg', models.TextField(blank=True, verbose_name='educational_background')),
                ('image', models.ImageField(blank=True, verbose_name='photo', null=True, upload_to='memberImg')),
                ('grade', models.CharField(verbose_name='年级', choices=[('1', 1), ('2', 2), ('3', 3), ('4', 4), ('5', 5)], max_length=2)),
                ('educational_level', models.CharField(verbose_name='学位（博士/硕士）', choices=[('master', '硕士'), ('doctor', '博士')], max_length=18)),
            ],
            options={
                'verbose_name': '学生信息',
                'db_table': 'PostgraduateEn',
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='Professor',
            fields=[
                ('id', models.AutoField(verbose_name='ID', primary_key=True, auto_created=True, serialize=False)),
                ('name', models.CharField(verbose_name='name', max_length=150)),
                ('Email', models.EmailField(blank=True, max_length=75)),
                ('address', models.CharField(blank=True, verbose_name='address', max_length=150)),
                ('postcode', models.CharField(verbose_name='postcode', default='000000', max_length=6)),
                ('edu_bg', models.TextField(blank=True, verbose_name='educational_background')),
                ('image', models.ImageField(blank=True, verbose_name='photo', null=True, upload_to='memberImg')),
                ('job_title', models.CharField(blank=True, verbose_name='职称', max_length=150)),
            ],
            options={
                'verbose_name': '老师信息',
                'db_table': 'Professor',
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='ProfessorEn',
            fields=[
                ('id', models.AutoField(verbose_name='ID', primary_key=True, auto_created=True, serialize=False)),
                ('name', models.CharField(verbose_name='name', max_length=150)),
                ('Email', models.EmailField(blank=True, max_length=75)),
                ('address', models.CharField(blank=True, verbose_name='address', max_length=150)),
                ('postcode', models.CharField(verbose_name='postcode', default='000000', max_length=6)),
                ('edu_bg', models.TextField(blank=True, verbose_name='educational_background')),
                ('image', models.ImageField(blank=True, verbose_name='photo', null=True, upload_to='memberImg')),
                ('job_title', models.CharField(blank=True, verbose_name='职称', max_length=150)),
            ],
            options={
                'verbose_name': '老师信息',
                'db_table': 'ProfessorEn',
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='PubInf',
            fields=[
                ('id', models.AutoField(verbose_name='ID', primary_key=True, auto_created=True, serialize=False)),
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
                ('id', models.AutoField(verbose_name='ID', primary_key=True, auto_created=True, serialize=False)),
                ('publish_info', models.TextField(blank=True, verbose_name='出版信息')),
                ('postgraduate', models.ForeignKey(to='bigdata.Postgraduate')),
            ],
            options={
                'db_table': 'PubInf1',
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='PubInf1En',
            fields=[
                ('id', models.AutoField(verbose_name='ID', primary_key=True, auto_created=True, serialize=False)),
                ('publish_info', models.TextField(blank=True, verbose_name='出版信息')),
                ('postgraduate', models.ForeignKey(to='bigdata.PostgraduateEn')),
            ],
            options={
                'db_table': 'PubInf1En',
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='PubInfEn',
            fields=[
                ('id', models.AutoField(verbose_name='ID', primary_key=True, auto_created=True, serialize=False)),
                ('publish_info', models.TextField(blank=True, verbose_name='出版信息')),
                ('professor', models.ForeignKey(to='bigdata.ProfessorEn')),
            ],
            options={
                'db_table': 'PubInfEn',
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='Relax',
            fields=[
                ('id', models.AutoField(verbose_name='ID', primary_key=True, auto_created=True, serialize=False)),
                ('title', models.CharField(null=True, max_length=150)),
                ('content', models.TextField(null=True)),
                ('time_stamp', models.DateTimeField(default=datetime.datetime(2015, 8, 7, 7, 9, 11, 281727, tzinfo=utc), auto_now_add=True)),
                ('picture', models.ImageField(blank=True, verbose_name='照片', null=True, upload_to='relax')),
            ],
            options={
                'verbose_name': '休闲活动',
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='RelaxEn',
            fields=[
                ('id', models.AutoField(verbose_name='ID', primary_key=True, auto_created=True, serialize=False)),
                ('title', models.CharField(null=True, max_length=150)),
                ('content', models.TextField(null=True)),
                ('time_stamp', models.DateTimeField(default=datetime.datetime(2015, 8, 7, 7, 9, 11, 293738, tzinfo=utc), auto_now_add=True)),
                ('picture', models.ImageField(blank=True, verbose_name='照片', null=True, upload_to='relax')),
            ],
            options={
                'verbose_name': '休闲活动',
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='ResAct',
            fields=[
                ('id', models.AutoField(verbose_name='ID', primary_key=True, auto_created=True, serialize=False)),
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
                ('id', models.AutoField(verbose_name='ID', primary_key=True, auto_created=True, serialize=False)),
                ('research_activity', models.TextField(blank=True, verbose_name='科研活动')),
                ('postgraduate', models.ForeignKey(to='bigdata.Postgraduate')),
            ],
            options={
                'db_table': 'ResAct1',
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='ResAct1En',
            fields=[
                ('id', models.AutoField(verbose_name='ID', primary_key=True, auto_created=True, serialize=False)),
                ('research_activity', models.TextField(blank=True, verbose_name='科研活动')),
                ('postgraduate', models.ForeignKey(to='bigdata.PostgraduateEn')),
            ],
            options={
                'db_table': 'ResAct1En',
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='ResActEn',
            fields=[
                ('id', models.AutoField(verbose_name='ID', primary_key=True, auto_created=True, serialize=False)),
                ('research_activity', models.TextField(blank=True, verbose_name='科研活动')),
                ('professor', models.ForeignKey(to='bigdata.ProfessorEn')),
            ],
            options={
                'db_table': 'ResActEn',
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='ResDir',
            fields=[
                ('id', models.AutoField(verbose_name='ID', primary_key=True, auto_created=True, serialize=False)),
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
                ('id', models.AutoField(verbose_name='ID', primary_key=True, auto_created=True, serialize=False)),
                ('research_direction', models.TextField(blank=True, verbose_name='研究方向')),
                ('postgraduate', models.ForeignKey(to='bigdata.Postgraduate')),
            ],
            options={
                'db_table': 'ResDir1',
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='ResDir1En',
            fields=[
                ('id', models.AutoField(verbose_name='ID', primary_key=True, auto_created=True, serialize=False)),
                ('research_direction', models.TextField(blank=True, verbose_name='研究方向')),
                ('postgraduate', models.ForeignKey(to='bigdata.PostgraduateEn')),
            ],
            options={
                'db_table': 'ResDir1En',
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='ResDirEn',
            fields=[
                ('id', models.AutoField(verbose_name='ID', primary_key=True, auto_created=True, serialize=False)),
                ('research_direction', models.TextField(blank=True, verbose_name='研究方向')),
                ('professor', models.ForeignKey(to='bigdata.ProfessorEn')),
            ],
            options={
                'db_table': 'ResDirEn',
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='WorkExp',
            fields=[
                ('id', models.AutoField(verbose_name='ID', primary_key=True, auto_created=True, serialize=False)),
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
                ('id', models.AutoField(verbose_name='ID', primary_key=True, auto_created=True, serialize=False)),
                ('work_experience', models.TextField(blank=True, verbose_name='工作经历')),
                ('postgraduate', models.ForeignKey(to='bigdata.Postgraduate')),
            ],
            options={
                'db_table': 'WorkExp1',
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='WorkExp1En',
            fields=[
                ('id', models.AutoField(verbose_name='ID', primary_key=True, auto_created=True, serialize=False)),
                ('work_experience', models.TextField(blank=True, verbose_name='工作经历')),
                ('postgraduate', models.ForeignKey(to='bigdata.PostgraduateEn')),
            ],
            options={
                'db_table': 'WorkExp1En',
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='WorkExpEn',
            fields=[
                ('id', models.AutoField(verbose_name='ID', primary_key=True, auto_created=True, serialize=False)),
                ('work_experience', models.TextField(blank=True, verbose_name='工作经历')),
                ('professor', models.ForeignKey(to='bigdata.ProfessorEn')),
            ],
            options={
                'db_table': 'WorkExpEn',
            },
            bases=(models.Model,),
        ),
        migrations.AddField(
            model_name='patprien',
            name='professor',
            field=models.ForeignKey(to='bigdata.ProfessorEn'),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='patpri1en',
            name='postgraduate',
            field=models.ForeignKey(to='bigdata.PostgraduateEn'),
            preserve_default=True,
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
            model_name='directionsen',
            name='lab',
            field=models.ForeignKey(to='bigdata.LabEn'),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='directions',
            name='lab',
            field=models.ForeignKey(to='bigdata.Lab'),
            preserve_default=True,
        ),
    ]
