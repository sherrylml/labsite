#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
__title__ = ''
__author__ = 'LML_CH'
__mtime__ = '2015/8/6'
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
import re

# with open(r'E:\git_workplace\labsite\labsite\bigdata\models\team_models.py', encoding='utf-8') as f,open(r'E:\git_workplace\labsite\labsite\bigdata\models\EnglishTeam_models.py','w',encoding='utf-8')as q:
#     for line in f:
#         temp = line
#         if re.match(r'class (.*)\(.*\):',temp):
#             print(temp)
#             name = re.match(r'class (.*)\(.*\):',temp).group(1)
#             print(name)
#             temp = temp.replace(name, name + 'En')
#         q.writelines(temp)

with open(r'E:\git_workplace\labsite\labsite\bigdata\models\EnglishTeam_models.py', encoding='utf-8') as f,open(r'E:\git_workplace\labsite\labsite\bigdata\models\EnglishTeam_models2.py','w',encoding='utf-8')as q:
    for line in f:
        temp = line
        if re.match(r'\s+db_table = \'(.*)\'',temp):
            print(temp)
            name = re.match(r'\s+db_table = \'(.*)\'',temp).group(1)
            print(name)
            temp = temp.replace(name, name + 'En')
        q.writelines(temp)
# db_table = 'Professor'