#coding:utf-8
from rest_framework import serializers
from django.contrib.auth.models import User
from framework.models import BOOK

#序列化用户
class User_serilizers(serializers.ModelSerializer):
    book = serializers.PrimaryKeyRelatedField(many=True,queryset=BOOK.objects.all())
    class Meta:
        model = User
        fields = ('id','username','book')

class BookSerializer(serializers.ModelSerializer):
    # owner = serializers.Field('owner.username')
    # owner = serializers.ReadOnlyField(source='owner.username')
    owner = serializers.ReadOnlyField(source="%(app_label)s_%(class)s_owner.username")
    class Meta:
        model = BOOK
        fields = ('id','name','author','title','owner','crate_date')
        # read_only_fields = ('modify_date',)

