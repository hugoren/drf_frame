#coding:utf-8

from django.db import models
import django.utils.timezone as timezone

# Create your models here.

#restful_api范例
class BOOK(models.Model):
    Book_name = models.CharField(max_length=100)
    Book_author = models.CharField(max_length=100)
    Book_title = models.CharField(max_length=100)
    crate_date = models.DateTimeField('保存日期',default = timezone.now)
    modify_date = models.DateTimeField('最后修改日期',auto_now = True)

    def __unicode__(self):
        return self.book_name


    class Meta:
        ordering = ('crate_date',)
