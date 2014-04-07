#coding=utf-8
#-*- coding: UTF-8 -*-

from django.conf.urls import patterns, include, url

from django.contrib import admin

from getLike.views import getDrama

admin.autodiscover()

urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'getLikeWeb.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),

    url(r'^admin/', include(admin.site.urls)),
    url(r'^$', getDrama),   #获取美剧更新路径
)
