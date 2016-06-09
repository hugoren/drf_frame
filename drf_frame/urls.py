#coding:utf-8

from django.conf.urls import include, url
from django.contrib import admin
from framework.views import *

urlpatterns = [
    url(r'^admin/', include(admin.site.urls)),
    #restful_api的apiview写法
    url(r'book/$',Book_list.as_view()),
    url(r'book_detail/(\d+)',Book_detail.as_view()),
    #restful_api的generic写法
    url(r'book_generic',Book_generic.as_view()),
]
