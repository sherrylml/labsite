from django.conf.urls import patterns,url
from bigdata import views
# from labsite.bigdata import views

urlpatterns = patterns('',
        url(r'^index$',  views.index, name='index'),
        url(r'^news$', views.news, name='news'),
        url(r'^team$', views.team, name='team')
    )


