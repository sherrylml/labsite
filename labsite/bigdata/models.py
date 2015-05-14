from django.db import models

# Create your models here.

class Members(models.Model):
    name = models.CharField(max_length=30)
    identity = models.CharField(max_length=30)
    homepage = models.URLField(null=True)

    def __str__(self):
        return self.name


class Team(models.Model):
    '''
    科研队伍
    '''
    team = []
    content = models.TextField()

    def __str__(self):
        return None


class Notation(models.Model):
    '''
    通知模板
    '''
    title = models.CharField(max_length=100)
    content = models.TextField()
    time_stamp = models.DateTimeField()
    link = models.URLField()

    def __str__(self):
        return self.title


class News(models.Model):
    '''
    新闻模板
    '''
    title = models.CharField(max_length=150)
    content = models.TextField()
    time_stamp = models.DateTimeField()
    link = models.URLField()

    def __str__(self):
        return self.title


class LearningMaterials(models.Model):
    '''
    科学研究、学术会议、学习资料
    '''
    title = models.CharField(max_length=100)
    introduction = models.TextField()
    download_link = models.URLField()

    def __str__(self):
        return self.title


class JoinUs(models.Model):
    '''
    招生信息, 人才招聘
    '''
    content = models.TextField()
    time_stamp = models.DateTimeField()


