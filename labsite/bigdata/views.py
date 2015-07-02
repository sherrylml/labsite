from django.http import HttpResponse
from django.shortcuts import render, render_to_response
from bigdata.models import News


def index(request):
    context = {}
    return render(request, 'bigdata/index.html', context)

def news(request):
    # newss = News.objects.all()
    newss = News.objects.order_by('time_stamp')
    context = {'newss':newss}
    return render_to_response('bigdata/news.html', context)
