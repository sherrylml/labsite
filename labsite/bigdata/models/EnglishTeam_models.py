from django.db import models
from django.utils.translation import gettext_lazy as _

class PeopleEn(models.Model):
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


class ProfessorEn(PeopleEn):
    job_title = models.CharField(max_length=150, blank=True, verbose_name='职称')

    class Meta:
        db_table = 'ProfessorEn'
        verbose_name = "老师信息(English)"


class VisitingProfessorEn(PeopleEn):
    job_title = models.CharField(max_length=150, blank=True, verbose_name='职称')

    class Meta:
        db_table = 'VisitingProfessorEn'
        verbose_name = "专家信息(English)"


class PostgraduateEn(PeopleEn):
    grade = models.CharField(max_length=2, choices=(zip([str(c) for c in range(1, 6)], range(1, 6))), verbose_name='年级')
    # grade = forms.ChoiceField(choices=list(range(8)))
    educational_level = models.CharField(max_length=18, choices=(('master', '硕士'), ('doctor', '博士')),
                                         verbose_name='学位（博士/硕士）')

    class Meta:
        db_table = 'PostgraduateEn'
        verbose_name = "学生信息(English)"


class ResDirEn(models.Model):
    research_direction = models.TextField(blank=True, verbose_name='研究方向')
    professor = models.ForeignKey(ProfessorEn)
    # postgraduate = models.ForeignKey(Postgraduate)

    def __str__(self):
        return str(self.id)

    class Meta:
        db_table = 'ResDirEn'
        # db_table = self.name


class WorkExpEn(models.Model):
    work_experience = models.TextField(blank=True, verbose_name='工作经历')
    professor = models.ForeignKey(ProfessorEn)

    class Meta:
        db_table = 'WorkExpEn'


class PatPriEn(models.Model):
    patent_prize = models.TextField(blank=True, verbose_name='专利与奖励')
    professor = models.ForeignKey(ProfessorEn)

    class Meta:
        db_table = 'PatPriEn'


class PubInfEn(models.Model):
    publish_info = models.TextField(blank=True, verbose_name='出版信息')
    professor = models.ForeignKey(ProfessorEn)

    class Meta:
        db_table = 'PubInfEn'


class ResActEn(models.Model):
    research_activity = models.TextField(blank=True, verbose_name='科研活动')
    professor = models.ForeignKey(ProfessorEn)

    class Meta:
        db_table = 'ResActEn'


class ResDir1En(models.Model):
    research_direction = models.TextField(blank=True, verbose_name='研究方向')
    postgraduate = models.ForeignKey(PostgraduateEn)

    def __str__(self):
        return str(self.id)

    class Meta:
        db_table = 'ResDir1En'


class WorkExp1En(models.Model):
    work_experience = models.TextField(blank=True, verbose_name='工作经历')
    postgraduate = models.ForeignKey(PostgraduateEn)

    class Meta:
        db_table = 'WorkExp1En'


class PatPri1En(models.Model):
    patent_prize = models.TextField(blank=True, verbose_name='专利与奖励')
    postgraduate = models.ForeignKey(PostgraduateEn)

    class Meta:
        db_table = 'PatPri1En'


class PubInf1En(models.Model):
    publish_info = models.TextField(blank=True, verbose_name='出版信息')
    postgraduate = models.ForeignKey(PostgraduateEn)

    class Meta:
        db_table = 'PubInf1En'


class ResAct1En(models.Model):
    research_activity = models.TextField(blank=True, verbose_name='科研活动')
    postgraduate = models.ForeignKey(PostgraduateEn)

    class Meta:
        db_table = 'ResAct1En'


class ResDir2En(models.Model):
    research_direction = models.TextField(blank=True, verbose_name='研究方向')
    professor = models.ForeignKey(VisitingProfessorEn)
    # postgraduate = models.ForeignKey(Postgraduate)

    def __str__(self):
        return str(self.id)

    class Meta:
        db_table = 'ResDir2En'
        # db_table = self.name


class WorkExp2En(models.Model):
    work_experience = models.TextField(blank=True, verbose_name='工作经历')
    professor = models.ForeignKey(VisitingProfessorEn)

    class Meta:
        db_table = 'WorkExp2En'


class PatPri2En(models.Model):
    patent_prize = models.TextField(blank=True, verbose_name='专利与奖励')
    professor = models.ForeignKey(VisitingProfessorEn)

    class Meta:
        db_table = 'PatPri2En'


class PubInf2En(models.Model):
    publish_info = models.TextField(blank=True, verbose_name='出版信息')
    professor = models.ForeignKey(VisitingProfessorEn)

    class Meta:
        db_table = 'PubInf2En'


class ResAct2En(models.Model):
    research_activity = models.TextField(blank=True, verbose_name='科研活动')
    professor = models.ForeignKey(VisitingProfessorEn)

    class Meta:
        db_table = 'ResAct2En'

