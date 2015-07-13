from django.conf.urls import patterns,url
from bigdata import views
# from labsite.bigdata import views

urlpatterns = patterns('',
        url(r'^index$',  views.index, name='index'),
        url(r'^news$', views.news, name='news'),
        url(r'^news/(?P<id>\d+)/$',views.news_detail, name='news_detail'),
        url(r'^notice/(?P<id>\d+)/$',views.notice_detail, name='notice_detail'),
        url(r'^team$', views.team, name='team'),
        url(r'^professor/(?P<id>\d+)/$',views.member_professor, name='member_professor'),
        url(r'^postgraduate/(?P<id>\d+)/$',views.member_postgraduate, name='member_postgraduate'),
        url(r'^research$', views.research, name='research'),
        url(r'^academic$', views.academic, name='academic'),
        url(r'^academic/(?P<id>\d+)/$',views.academic_detail, name='academic_detail'),
        url(r'^relax/(?P<id>\d+)/$', views.relax, name='relax'),
        url(r'^join$', views.join, name='join'),
        url(r'^about$', views.about, name='about'),
    )


