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


class People(models.Model):
    name = models.CharField(max_length=150, verbose_name='姓名')
    # ('id', models.AutoField(serialize=False, primary_key=True, auto_created=True))
    Email = models.EmailField()
    mainpage = models.URLField(blank=True, verbose_name='个人主页')

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
    grade = models.CharField(max_length=1, verbose_name='年级')
    educational_level = models.CharField(max_length=18, verbose_name='学位（博士/硕士）')
    # grade = forms.ChoiceField(choices=list(range(8)))

