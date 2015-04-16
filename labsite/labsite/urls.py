from django.conf.urls import patterns, include, url
from django.contrib import admin

urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'labsite.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),
    url(r'^bigdata/',include('bigdata.urls')),
    url(r'^admin/', include(admin.site.urls)),
)
