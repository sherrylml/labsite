from django.conf.urls import patterns, include, url
from django.conf.urls.i18n import i18n_patterns
from django.contrib import admin

from django.conf.urls.static import static
from django.conf import settings
from django.core.urlresolvers import LocaleRegexURLResolver

urlpatterns = patterns(
    '',
    url(r'^$', include('bigdata.urls')),

    url(r'^admin/', include(admin.site.urls), name='admin'),

    url(r'^i18n/', include('django.conf.urls.i18n')),
    url(r'hitcount/', include('hitcount.urls', namespace='hitcount')),
    # url(r'^set_language/$', 'django.views.i18n.set_language', name='set_language'),
)

# + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
