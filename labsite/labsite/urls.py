from django.conf.urls import patterns, include, url
from django.contrib import admin

from django.conf.urls.static import static
from django.conf import settings

urlpatterns = patterns('',
    # url(r'^bigdata/',include('bigdata.urls')),
    url(r'^$', 'bigdata.views.index_e', name='index_e'),
    url(r'^chinesepage$', 'bigdata.views.index', name='index'),
    url(r'^news$', 'bigdata.views.news', name='news'),
    url(r'^news/(?P<id>\d+)/$','bigdata.views.news_detail', name='news_detail'),
    url(r'^notice/(?P<id>\d+)/$','bigdata.views.notice_detail', name='notice_detail'),
    url(r'^team$', 'bigdata.views.team', name='team'),
    url(r'^professor/(?P<id>\d+)/$','bigdata.views.member_professor', name='member_professor'),
    url(r'^postgraduate/(?P<id>\d+)/$','bigdata.views.member_postgraduate', name='member_postgraduate'),
    url(r'^research$','bigdata.views.research', name='research'),
    url(r'^academic$', 'bigdata.views.academic', name='academic'),
    url(r'^academic/(?P<id>\d+)/$','bigdata.views.academic_detail', name='academic_detail'),
    url(r'^relax/(?P<id>\d+)/$', 'bigdata.views.relax', name='relax'),
    url(r'^join$', 'bigdata.views.join', name='join'),
    url(r'^about$', 'bigdata.views.about', name='about'),

    url(r'^admin/', include(admin.site.urls), name='admin'),
)
              # + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
