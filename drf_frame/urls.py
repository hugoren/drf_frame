#coding:utf-8

from django.conf.urls import include, url
from django.contrib import admin

from rest_framework import routers
from rest_framework.authtoken import views as tokenviews

from framework.views import *
from framework import views
from framework import test_permissions
from framework import dbCenter
from framework import tasks

from webui import views as webviews


# 路由注册
router = routers.DefaultRouter()
router.register(r'bookViewset', views.BookViewsets)
# # urlpatterns = router.urls

from django.contrib import admin
admin.autodiscover()

urlpatterns = [


    #webui
    url(r'^', include('webui.urls')),

    #api token认证
    url(r'^api/token/$', tokenviews.obtain_auth_token),

    # #日志数据api接入
    url(r'^mission/dr/$',dbCenter.dr),
    url(r'^mission/dread/$',tasks.DBREAD.as_view()),

    #测试权限
    url(r'^p1/$', test_permissions.permission1().as_view()),
    url(r'^p2/$', test_permissions.permission2),


    url(r'^api-auth/', include('rest_framework.urls', namespace='rest_framework')),


    url(r'^admin/', include(admin.site.urls)),

    #ApiView装饰符带参数增删查改
    url(r'^bookApi/(?P<pk>[0-9]+)/$',bookApi),

    #ApiViewg不带装饰符带参数增删查改
    url(r'^bookApiView/(?P<pk>[0-9]+)/$',BookApiView.as_view()),
    url(r'^BookList/$',Book_list.as_view()),

    #restful_api的generic写法
    url(r'bookGeneric',BookGenerics.as_view()),

    #路由模式,viewset
    url(r'^r/',include(router.urls)),

    #mixins模式
    url(r'^bookMixins',BookMixins.as_view()),


]
