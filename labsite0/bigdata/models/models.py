from django.db import models

# Create your models here.
from django.utils import timezone


# class Base(models.Model):
#     '''
#     基类
#     '''
#     # title = models.CharField(max_length=150, default='')
#     title = models.CharField(max_length=150, null=True)
#     content = models.TextField(null=True)
#     time_stamp = models.DateTimeField(auto_now_add=True, default=timezone.now())
#     link = models.URLField(blank=True, verbose_name='url_link')
#
#     class Meta:
#         abstract = True
#
#     def __str__(self):
#         return self.title
#
#
# class News(Base):
#     '''
#     新闻模板
#     '''
#     pass

class News(models.Model):
    title = models.CharField(max_length=150, null=True)
    content = models.TextField(null=True)
    time_stamp = models.DateTimeField(auto_now_add=True, default=timezone.now())
    def __str__(self):
        return self.title