from django.conf.urls import patterns,url
from bigdata import views
# from labsite.bigdata import views

urlpatterns = patterns('',
        url(r'^index$',  views.index, name='index'),
        url(r'^news$', views.news, name='news'),
        url(r'^team$', views.team, name='team'),
        url(r'^research$', views.research, name='research'),
        url(r'^academic$', views.academic, name='academic'),
        url(r'^relax$', views.relax, name='relax'),
        url(r'^join$', views.join, name='join'),
        url(r'^about$', views.about, name='about'),
    )


