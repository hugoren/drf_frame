#coding:utf-8
from __future__ import absolute_import


from framework.tasks import add
from framework.tasks import DBREAD
from framework.tasks import input_queue_data

def call_tasks(n,m):
    try:
        r = add.delay(n,m)
        print r
    except Exception as e:
        print e


'''
直接调用api_post过来数据
'''
def call_db():
    try:
        r = DBREAD().post.delay(None,None)
        return r
    except Exception as e:
        print e

'''
间接调用api_post过来数据
'''
def write_into_db():
    try:
        r = input_queue_data.delay()
        return r
    except Exception as e:
        return e

