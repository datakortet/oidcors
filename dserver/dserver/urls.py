from django.conf.urls import patterns, include, url
from django.contrib import admin

urlpatterns = patterns('',
    url(r'^$', 'dserver.views.home', name='home'),
    url(r'^djson/$', 'dserver.views.djson', name='djson'),

    url(r'^admin/', include(admin.site.urls)),
)
