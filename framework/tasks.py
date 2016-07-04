#coding:utf-8
from __future__ import absolute_import

from drf_frame.celery import app
from celery import  shared_task
from celery import  task
from celery.contrib.methods import task as ctask

from rest_framework.decorators import api_view, permission_classes
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from rest_framework.views import APIView

from framework.models import YMATOULOG
from framework import  redis_queue


'''
1.接受api数据
2.存入redis队列
'''
class DBREAD(APIView):
    permission_classes = (IsAuthenticated,)

    def post(self, req):
        try:
            if req.method == 'POST':

                operater = req.POST.get('operater')
                message = req.POST.get('message')
                r_dict = {'operater':operater,'message':message}

                '''
                数据写入redis队列
                '''
                r = redis_queue.RedisQueue('log')
                r.put(r_dict)

                # '''
                # 取队列数据入库
                # '''
                # q = r.get()
                # q_dict = eval(q)
                # write_db = YMATOULOG(operater=q_dict['operater'],app='test',message=q_dict['message'])
                # write_db.save()

                return Response('success')

            else:
                return Response('只接受post请求')
        except Exception as e:
            return Response(e.message)

'''
1.从队列取数据
2.异步存入mysql
'''

@shared_task
def get_redis_queue():
    '''
     取队列数据入库
    '''
    r = redis_queue.RedisQueue('log')
    q = r.get()
    q_dict = eval(q)
    write_db = YMATOULOG(operater=q_dict['operater'],app='test',message=q_dict['message'])
    write_db.save()