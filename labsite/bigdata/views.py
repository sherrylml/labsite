from django.http import HttpResponse
from django.shortcuts import render, render_to_response
from .models.models import News,Notices
from .models.team_models import Professor, Postgraduate


def index(request):
    Month = {1:'JAN', 2:'FEB',3:'MAR', 4:'APR', 5:'MAY',6:'JUN',7:'JUL',8:'AUG',9:'SEP',10:'OCT',11:'NOV',12:'DEC'}
    news_list = News.objects.all().order_by('-time_stamp')[0:4]
    notices_list = Notices.objects.all().order_by('-time_stamp')[0:4]
    Context = {'news_list':news_list,'notices_list':notices_list,'Month':Month}
    return render(request, 'bigdata/index.html', Context)


def news(request):
    newss = News.objects.order_by('-time_stamp')
    context = {'newss': newss}
    return render_to_response('bigdata/news-pi.html', context)


def team(request):
    professors = Professor.objects.all()
    masters = Postgraduate.objects.filter()
    doctors = Postgraduate.objects.filter()
    return render_to_response('bigdata/team-pi.html', locals())

