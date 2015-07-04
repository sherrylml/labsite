from django.http import HttpResponse
from django.shortcuts import render, render_to_response
from .models.models import News
from .models.team_models import Professor, Postgraduate


def index(request):
    context = {}
    return render(request, 'bigdata/index.html', context)


def news(request):
    newss = News.objects.order_by('time_stamp')
    context = {'newss': newss}
    return render_to_response('bigdata/news-pi.html', context)


def team(request):
    professors = Professor.objects.all()
    masters = Postgraduate.objects.filter()
    doctors = Postgraduate.objects.filter()
    return render_to_response('bigdata/team-pi.html', professors, masters, doctors)

