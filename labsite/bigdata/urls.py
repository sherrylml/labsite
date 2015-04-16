from django.conf.urls import patterns,url
from bigdata import views
# from labsite.bigdata import views

urlpatterns = patterns('',
        url(r'^$',  views.index, name='index'),
    )


