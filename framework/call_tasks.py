#coding:utf-8
from __future__ import absolute_import
from framework import tasks
from datetime import timedelta
from framework.tasks import DBREAD
from framework.tasks import get_redis_queue


'''
redis队列数据入库
'''

def input_mysql():
    in_data = tasks.get_redis_queue.delay()


