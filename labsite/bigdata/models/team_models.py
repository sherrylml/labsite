from django.db import models
from django.utils.translation import gettext_lazy as _


class People(models.Model):
    name = models.CharField(max_length=150, verbose_name=_('name'))
    # ('id', models.AutoField(serialize=False, primary_key=True, auto_created=True))
    Email = models.EmailField(blank=True)
    # mainpage = models.URLField(blank=True, verbose_name='个人主页')
    address = models.CharField(blank=True, max_length=150, verbose_name=_('address'))
    postcode = models.CharField(default='000000', max_length=6, verbose_name=_('postcode'))
    edu_bg = models.TextField(blank=True, verbose_name=_('educational_background'))
    image = models.ImageField(upload_to='memberImg', blank=True, null=True, verbose_name=_('photo'))

    class Meta:
        abstract = True

    def __str__(self):
        return self.name


class Professor(People):
    job_title = models.CharField(max_length=150, blank=True, verbose_name='职称')

    class Meta:
        db_table = 'Professor'
        verbose_name = "老师信息"


class Postgraduate(People):
    grade = models.CharField(max_length=2, choices=(zip([str(c) for c in range(1, 6)], range(1, 6))), verbose_name='年级')
    # grade = forms.ChoiceField(choices=list(range(8)))
    educational_level = models.CharField(max_length=18, choices=(('master', '硕士'), ('doctor', '博士')),
                                         verbose_name='学位（博士/硕士）')

    class Meta:
        db_table = 'Postgraduate'
        verbose_name = "学生信息"


class ResDir(models.Model):
    research_direction = models.TextField(blank=True, verbose_name='研究方向')
    professor = models.ForeignKey(Professor)
    # postgraduate = models.ForeignKey(Postgraduate)

    def __str__(self):
        return str(self.id)

    class Meta:
        db_table = 'ResDir'
        # db_table = self.name


class WorkExp(models.Model):
    work_experience = models.TextField(blank=True, verbose_name='工作经历')
    professor = models.ForeignKey(Professor)

    class Meta:
        db_table = 'WorkExp'


class PatPri(models.Model):
    patent_prize = models.TextField(blank=True, verbose_name='专利与奖励')
    professor = models.ForeignKey(Professor)

    class Meta:
        db_table = 'PatPri'


class PubInf(models.Model):
    publish_info = models.TextField(blank=True, verbose_name='出版信息')
    professor = models.ForeignKey(Professor)

    class Meta:
        db_table = 'PubInf'


class ResAct(models.Model):
    research_activity = models.TextField(blank=True, verbose_name='科研活动')
    professor = models.ForeignKey(Professor)

    class Meta:
        db_table = 'ResAct'


class ResDir1(models.Model):
    research_direction = models.TextField(blank=True, verbose_name='研究方向')
    postgraduate = models.ForeignKey(Postgraduate)

    def __str__(self):
        return str(self.id)

    class Meta:
        db_table = 'ResDir1'


class WorkExp1(models.Model):
    work_experience = models.TextField(blank=True, verbose_name='工作经历')
    postgraduate = models.ForeignKey(Postgraduate)

    class Meta:
        db_table = 'WorkExp1'


class PatPri1(models.Model):
    patent_prize = models.TextField(blank=True, verbose_name='专利与奖励')
    postgraduate = models.ForeignKey(Postgraduate)

    class Meta:
        db_table = 'PatPri1'


class PubInf1(models.Model):
    publish_info = models.TextField(blank=True, verbose_name='出版信息')
    postgraduate = models.ForeignKey(Postgraduate)

    class Meta:
        db_table = 'PubInf1'


class ResAct1(models.Model):
    research_activity = models.TextField(blank=True, verbose_name='科研活动')
    postgraduate = models.ForeignKey(Postgraduate)

    class Meta:
        db_table = 'ResAct1'

