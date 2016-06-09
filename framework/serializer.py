#coding:utf-8
from rest_framework import serializers
from framework.models import BOOK

class BookSerializer(serializers.ModelSerializer):

    class Meta:
        model = BOOK
        fields = ('id','Book_name','Book_author','Book_title','crate_date','modify_date')