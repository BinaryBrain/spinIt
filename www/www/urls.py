from django.conf.urls import patterns, include, url
from django.contrib import admin
from django.http import HttpResponseRedirect
from django.conf import settings

urlpatterns = patterns('',
                       url(r"^admin/", include(admin.site.urls)),
                       url("^$", "main.views.index.index")
                       )
