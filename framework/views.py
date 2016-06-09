#coding:utf-8
from django.shortcuts import render

# Create your views here.
from django.http import HttpResponse
from django.contrib.auth.models import User
from rest_framework.renderers import JSONRenderer
from rest_framework import status
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework import  generics
from framework.models import BOOK
from framework.serializer import BookSerializer

#restful_api模版
# class JSONResponse(HttpResponse):
#     def __init__(self,data,**kwargs):
#         content = JSONRenderer().render(data)
#         kwargs['content_type'] = 'application/json'
#         super(JSONResponse,self).__init__(content,**kwargs)


# 通用视图写法
# class book(generics.ListCreateAPIView):
#     queryset = BOOK.objects.all()
#     serializer_class = BookSerializer


# def getbook(generics.List):
#     queryset = BOOK.objects.all()
#     serializer_class = BookSerializer


#APIView写法
class Book_list(APIView):

    def get(self,request,format=None):
        books = BOOK.objects.all()
        ser = BookSerializer(books,many=True)
        return Response(ser.data)

    def post(self,request,format):
        ser = BookSerializer(request.DATA)
        if ser.is_valid():
            ser.save()
            return Response(ser.data)
        return Response(ser.errors)

#单个查询
class Book_detail(APIView):
    def get_detail(self,request,num,format=None):
        books = BOOK.objects.get(id=num)
        ser = BookSerializer(books)
        return  Response(ser.data)


#通用视图写法
class Book_generic(generics.ListCreateAPIView):
    queryset = BOOK.objects.all()
    serializer_class = BookSerializer

# @api_view(['GET','POST','PUT','UPDATE','DELETE'])
# def book_detail(request):
#     try:
#         queryset = BOOK.objects.all()
#         print queryset['author']
#     except Exception as e:
#         return Response(status=status.HTTP_404_NOT_FOUND)
#
#     if request.method == 'GET':
#         serializer = BookSerializer(queryset)
#         return Response(serializer.data)
#
#     elif request.method == 'POST':
#         serializer = BookSerializer(data=request.DATA)
#         if serializer.is_valid():
#             serializer.save()
#             return JSONResponse(serializer.data,status=status.HTTP_201_CREATED)
#         else:
#             return JSONResponse(serializer.errors,status=status.HTTP_400_BAD_REQUEST)
#
#     elif request.method == 'PUT':
#         serializer = BookSerializer(book_object,data=request.DATA)
#         if serializer.is_valid():
#             serializer.save()
#             return JSONResponse(serializer.data)
#         else:
#             return JSONResponse(serializer.errors,status=status.HTTP_400_BAD_REQUEST)
#
#     elif request.method == 'DELETE':
#         Book.delete()
#         return JSONResponse(status=status.HTTP_204_NO_CONTENT)
#     elif request.method == 'UPDATE':
#         pass
#     else:
#         pass