from django.http import HttpResponse
from django.shortcuts import render, render_to_response
from .models.models import News,Notices,Academic,Meetings,Relax
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
    Context = {'news_list':news_list,'notices_list':notices_list,'Month':Month}
    return render(request, 'bigdata/index.html', Context)


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

def research(request):
    '''
    科学研究
    '''
    Context = {}
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
    Context = {}
    return render_to_response('bigdata/join.html', Context)

def about(request):
    '''
    关于
    '''
    Context = {}
    return render_to_response('bigdata/about.html', Context)


