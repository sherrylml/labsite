#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
__title__ = ''
__author__ = 'pi'
__mtime__ = '7/4/2015-004'
# code is far away from bugs with the god animal protecting
    I love animals. They taste delicious.
              ┏┓      ┏┓
            ┏┛┻━━━┛┻┓
            ┃      ☃      ┃
            ┃  ┳┛  ┗┳  ┃
            ┃      ┻      ┃
            ┗━┓      ┏━┛
                ┃      ┗━━━┓
                ┃  神兽保佑    ┣┓
                ┃　永无BUG！   ┏┛
                ┗┓┓┏━┳┓┏┛
                  ┃┫┫  ┃┫┫
                  ┗┻┛  ┗┻┛
"""
from django.db import models


class Publisher(models.Model):
    name = models.CharField(max_length=25)
    address = models.CharField(max_length=30)


class People(models.Model):
    name = models.CharField(max_length=150, verbose_name='姓名')
    # ('id', models.AutoField(serialize=False, primary_key=True, auto_created=True))
    Email = models.EmailField(blank=True)
    mainpage = models.URLField(blank=True, verbose_name='个人主页')
    address = models.CharField(blank=True, max_length=150, verbose_name='通信地址')
    postcode = models.CharField(default='000000', max_length=6, verbose_name='邮政编码')
    edu_bg = models.TextField(blank=True, verbose_name='教育背景')
    image = models.ImageField(null=True, verbose_name='个人照片')

    research_direction = models.TextField(blank=True, verbose_name='研究方向')
    work_experience = models.TextField(blank=True, verbose_name='工作经历')
    patent_prize = models.TextField(blank=True, verbose_name='专利与奖励')
    publish_infor = models.TextField(blank=True, verbose_name='出版信息')
    publisher = models.ForeignKey(Publisher)
    research_activities = models.TextField(blank=True, verbose_name='科研活动')

    class Meta:
        '''
        不创建表
        '''
        abstract = True

    def __str__(self):
        return self.name


class Professor(People):
    # name = models.CharField(max_length=150, verbose_name='姓名')
    # django.core.exceptions.FieldError: Local field 'name' in class 'Professor' clashes with field of similar name from base class 'People'
    job_title = models.CharField(max_length=150, null=True, verbose_name='职称')


class Postgraduate(People):
    grade = models.CharField(max_length=1, choices=(tuple(zip(range(1, 6), range(1, 6)))), verbose_name='年级')
    educational_level = models.CharField(max_length=18, choices=(('master', '硕士'), ('doctor', '博士')),
                                         verbose_name='学位（博士/硕士）')
    # grade = forms.ChoiceField(choices=list(range(8)))
