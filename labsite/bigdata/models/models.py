from django.db import models

# Create your models here.
from django.utils import timezone


class Base(models.Model):
    '''
    基类
    '''
    # item_id = models.AutoField(primary_key=True,default=1)
    title = models.CharField(max_length=150, null=True)
    title_en = models.CharField(max_length=150, null=True)
    content = models.TextField(null=True)
    content_en = models.TextField(null=True)
    time_stamp = models.DateTimeField(auto_now_add=True, default=timezone.now())

    class Meta:
        abstract = True

    def __str__(self):
        return self.title


class News(Base):
    '''
    新闻模板
    '''
    picture = models.ImageField(upload_to='news', blank=True, null=True, verbose_name='照片')

    class Meta:
        verbose_name = "新闻动态"


class Notices(Base):
    '''
    通知模板
    '''
    picture = models.ImageField(upload_to='notices', blank=True, null=True, verbose_name='照片')

    class Meta:
        verbose_name = "通知公告"


class Academic(Base):
    '''
    学术交流
    '''
    picture = models.ImageField(upload_to='academic', blank=True, null=True, verbose_name='照片')

    class Meta:
        verbose_name = "学术交流活动"


class Meetings(Base):
    '''
    学术会议
    '''
    link = models.URLField(blank=True, verbose_name='url_link')

    class Meta:
        verbose_name = "近期学术会议"


class Relax(Base):
    '''
    活动休闲
    '''
    picture = models.ImageField(upload_to='relax', blank=True, null=True, verbose_name='照片')

    class Meta:
        verbose_name = "休闲活动"


class Join1(Base):
    '''
    招生信息
    '''

    class Meta:
        verbose_name = "招生信息"


class Join2(Base):
    '''
    招聘信息
    '''

    class Meta:
        verbose_name = "人才招聘"


# 相关信息
class Lab(models.Model):
    '''
    简介+研究方向+研究成果
    '''
    introduction = models.TextField(null=True)
    introduction_en = models.TextField(null=True)
    achievement = models.TextField(null=True)

    class Meta:
        verbose_name = "研究组相关信息"

    def __str__(self):
        # return "实验室相关信息" + str(self.id)
        return "研究组相关信息"



class Directions(models.Model):
    research_direction = models.TextField(blank=True, verbose_name='研究方向')
    lab = models.ForeignKey(Lab)


    def __str__(self):
        return str(self.id)

    class Meta:
        db_table = 'Directions'
        # db_table = self.name


class Images(models.Model):
    images = models.ImageField(upload_to='research_direction', blank=True, null=True, verbose_name='图片')
    directions = models.ForeignKey(Directions)
    # lab = models.ForeignKey(Lab)

    def __str__(self):
        return str(self.id)

    class Meta:
        db_table = 'Images'
        # db_table = self.name

