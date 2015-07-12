from django.db import models

# Create your models here.
from django.utils import timezone


class Base(models.Model):
    '''
    基类
    '''
    # item_id = models.AutoField(primary_key=True,default=1)
    title = models.CharField(max_length=150, null=True)
    content = models.TextField(null=True)
    time_stamp = models.DateTimeField(auto_now_add=True, default=timezone.now())

    class Meta:
        abstract = True

    def __str__(self):
        return self.title


class News(Base):
    '''
    新闻模板
    '''
    picture = models.ImageField(upload_to='news',blank=True, null=True, verbose_name='照片')

class Notices(Base):
    '''
    通知模板
    '''
    picture = models.ImageField(upload_to='notices',blank=True, null=True, verbose_name='照片')

class Academic(Base):
    '''
    学术交流
    '''
    picture = models.ImageField(upload_to='academic',blank=True, null=True, verbose_name='照片')

class Meetings(Base):
    '''
    学术会议
    '''
    link = models.URLField(blank=True, verbose_name='url_link')

class Relax(Base):
    '''
    活动休闲
    '''
    picture = models.ImageField(upload_to='relax',blank=True, null=True, verbose_name='照片')

class Join1(Base):
    '''
    招生信息
    '''
    pass

class Join2(Base):
    '''
    招聘信息
    '''
    pass

# 实验室相关信息
class Lab(models.Model):
    '''
    实验室简介+研究方向+研究成果
    '''
    introduction = models.TextField(null=True)
    direction = models.TextField(null=True)
    achievement = models.TextField(null=True)

    def __str__(self):
        return "实验室相关信息" + str(self.id)