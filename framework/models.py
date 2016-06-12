#coding:utf-8

from django.db import models
from django.contrib.auth.models import User

#restful_api范例
class BOOK(models.Model):
    name = models.CharField(max_length=100)
    author = models.CharField(max_length=100)
    title = models.CharField(max_length=100)
    crate_date = models.DateTimeField('保存日期',auto_now_add = True)
    modify_date = models.DateTimeField('最后修改日期',auto_now = True)
    # owner = models.ForeignKey('auth.User',related_name='book',null=True, blank=True)
    owner = models.ForeignKey('auth.User',related_name='%(app_label)s_%(class)s_owner', verbose_name='owner', blank=True,null=True)
    # owner = models.ForeignKey('auth.User',related_name='book', verbose_name='owner',)

    def __unicode__(self):
        return self.name
    #
    # class Meta:
    #     ordering = ('id',)
