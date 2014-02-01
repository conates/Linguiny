from django.conf.urls import patterns, include, url

from django.contrib import admin
admin.autodiscover()

urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'Linguiny.views.home', name='home'),
    url(r'^$', 'frontend.views.home', name='home'),
    url(r'^results.html/$', 'frontend.views.results', name='results'),
    url(r'^profile.html/(\d+)/$', 'frontend.views.profile', name='profile'),
    url(r'^admin/', include(admin.site.urls)),
)