#coding:utf-8

from django.conf.urls import include, url
from django.contrib import admin
from framework.views import *
from rest_framework import routers
from framework import views

#路由注册
router = routers.DefaultRouter()
router.register(r'book', views.BookViewsets)
# # urlpatterns = router.urls

urlpatterns = [
    url(r'^admin/', include(admin.site.urls)),

    #restful_api的apiview写法
    # url(r'book/$',Book_list.as_view()),
    # url(r'book_detail/(\d+)',Book_detail.as_view()),

    #restful_api的generic写法
    url(r'bookGeneric',BookGenerics.as_view()),

    #路由模式
    url(r'^',include(router.urls)),

    url(r'^api-auth/', include('rest_framework.urls', namespace='rest_framework'))
]
