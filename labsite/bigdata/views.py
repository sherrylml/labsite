from django.http import HttpResponse
from django.shortcuts import render, render_to_response
from .models.models import *
from .models.team_models import Professor, Postgraduate


def index(request):
    '''
    首页
    '''
    Month = {1:'JAN', 2:'FEB',3:'MAR', 4:'APR', 5:'MAY',6:'JUN',7:'JUL',8:'AUG',9:'SEP',10:'OCT',11:'NOV',12:'DEC'}
    news_list = News.objects.all().order_by('-time_stamp')
    if len(news_list) > 3:
        news_list = news_list[0:4]
    notices_list = Notices.objects.all().order_by('-time_stamp')
    if len(notices_list) > 3:
        notices_list = notices_list[0:4]
    meetings_list = Meetings.objects.all()
    join1_list = Join1.objects.order_by('-time_stamp')
    join2_list = Join2.objects.order_by('-time_stamp')
    lab_intro = Lab.objects.order_by('-id')[0].introduction
    return render(request, 'bigdata/index.html', locals())


def news(request):
    '''
    通知&新闻
    '''
    news_list = News.objects.order_by('-time_stamp')
    notices_list = Notices.objects.order_by('-time_stamp')
    return render_to_response('bigdata/news.html', locals())

def news_detail(request, id):
    '''
    新闻详情
    '''
    item_id = int(id)
    news = News.objects.get(id = item_id)
    Month = {1:'JAN', 2:'FEB',3:'MAR', 4:'APR', 5:'MAY',6:'JUN',7:'JUL',8:'AUG',9:'SEP',10:'OCT',11:'NOV',12:'DEC'}
    Context = {'news':news, 'Month':Month}
    return render_to_response('bigdata/news_detail.html', Context)

def notice_detail(request, id):
    '''
    通知详情
    '''
    item_id = int(id)
    notice = Notices.objects.get(id = item_id)
    Month = {1:'JAN', 2:'FEB',3:'MAR', 4:'APR', 5:'MAY',6:'JUN',7:'JUL',8:'AUG',9:'SEP',10:'OCT',11:'NOV',12:'DEC'}
    Context = {'notice':notice, 'Month':Month}
    return render_to_response('bigdata/notice_detail.html', Context)

def team(request):
    '''
    科研团队
    '''
    professors_list = Professor.objects.all()
    masters_list = Postgraduate.objects.filter()
    doctors_list = Postgraduate.objects.filter()
    return render_to_response('bigdata/team.html', locals())

def member_professor(request, id):
    '''
    个人主页
    '''
    item_id = int(id)
    member = Professor.objects.get(id = item_id)
    Context = {'member': member}
    return render_to_response('bigdata/member.html', Context)

def member_postgraduate(request, id):
    '''
    个人主页
    '''
    item_id = int(id)
    member = Postgraduate.objects.get(id = item_id)
    Context = {'member': member}
    return render_to_response('bigdata/member.html', Context)

def research(request):
    '''
    科学研究
    '''
    lab = Lab.objects.order_by('-id')[0]
    research_direction = lab.direction
    research_achievement = lab.achievement
    Context = {'research_direction':research_direction, 'research_achievement':research_achievement}
    return render_to_response('bigdata/research.html', Context)

def academic(request):
    '''
    合作交流
    '''
    academic_list = Academic.objects.all()
    meetings_list = Meetings.objects.all()
    return render_to_response('bigdata/academic.html', locals())

def academic_detail(request, id):
    '''
    学术交流活动详情
    '''
    item_id = int(id)
    academic = Academic.objects.get(id = item_id)
    Month = {1:'JAN', 2:'FEB',3:'MAR', 4:'APR', 5:'MAY',6:'JUN',7:'JUL',8:'AUG',9:'SEP',10:'OCT',11:'NOV',12:'DEC'}
    Context = {'academic':academic, 'Month':Month}
    return render_to_response('bigdata/academic_detail.html', Context)

def relax(request):
    '''
    活动休闲
    '''
    relax_list = Relax.objects.all()
    Month = {1:'JAN', 2:'FEB',3:'MAR', 4:'APR', 5:'MAY',6:'JUN',7:'JUL',8:'AUG',9:'SEP',10:'OCT',11:'NOV',12:'DEC'}
    Context = {'relax_list':relax_list, 'Month':Month}
    return render_to_response('bigdata/relax.html', Context)

def join(request):
    '''
    加入我们
    '''
    join1_list = Join1.objects.order_by('-time_stamp')
    join2_list = Join2.objects.order_by('-time_stamp')
    return render_to_response('bigdata/join.html', locals())

def about(request):
    '''
    关于
    '''
    lab = Lab.objects.order_by('-id')[0]
    lab_intro = lab.introduction
    Context = {'lab_intro':lab_intro}
    return render_to_response('bigdata/about.html', Context)


