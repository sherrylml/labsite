#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
__title__ = ''
__author__ = 'LML_CH'
__mtime__ = '2015/7/12'
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

from django.utils import timezone

# class Base(models.Model):
#     '''
#     基类
#     '''
#     # item_id = models.AutoField(primary_key=True,default=1)
#     title = models.CharField(max_length=150, null=True)
#     content = models.TextField(null=True)
#     time_stamp = models.DateTimeField(auto_now_add=True, default=timezone.now())
#
#     class Meta:
#         abstract = True
#
#     def __str__(self):
#         return self.title
#
# class LabIntro(Base):
#     '''
#     实验室简介
#     '''
#     pass
#
# class ResearchField(Base):
#     '''
#     研究方向
#     '''
#     pass
#
# class ResearchResult(Base):
#     '''
#     研究成果
#     '''
#     pass