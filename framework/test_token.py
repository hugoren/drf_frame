#coding:utf-8

import requests
import simplejson as json
import time

def test_token():
    api_token = requests.post('http://localhost:10000/api/token/', data={'username': 'hugo','password':'hugo9091'})
    token = json.loads(api_token.content)['token']
    return token


def test_p2():
    token = '1a5367f62221575fdd35921f2364d18f551a8501'
    p2_get = requests.get('http://127.0.0.1:10000/p2/',headers={'Authorization': ('Token {0}'.format(token))})
    package_api_response = json.loads(p2_get.content)
    try:
        # status = package_api_response['results'][0]['status']
        print package_api_response
    except Exception as e:
        print e.message


def test_p3():
    try:
        token = '1a5367f62221575fdd35921f2364d18f551a8501'
        payload = {'operater':'hugo',}
        p3_json=requests.post('http://127.0.0.1:10000/p2/',headers={'Authorization': ('Token {0}'.format(token))},data = payload)
        p3 = json.loads(p3_json.content)
        print p3
    except Exception as e:
        print e

def test_data():
    try:
        token = '1a5367f62221575fdd35921f2364d18f551a8501'
        payload = {'operater':'hugo',}
        p3_json=requests.post('http://127.0.0.1:10000/mission/dr/',headers={'Authorization': ('Token {0}'.format(token))},data = payload)
        p3 = json.loads(p3_json.content)
        print p3
    except Exception as e:
        print e

def get_data():
    try:
        token = '1a5367f62221575fdd35921f2364d18f551a8501'
        payload = {'operater':'hugo_post9999',}
        p4_json=requests.get('http://127.0.0.1:10000/mission/dread/',headers={'Authorization': ('Token {0}'.format(token))})
        p4 = json.loads(p4_json.content)
        print p4
    except Exception as e:
        print e




def d_data():
    try:
        token = '1a5367f62221575fdd35921f2364d18f551a8501'
        payload = {'operater':'@post',}
        p4_json=requests.post('http://127.0.0.1:10000/mission/dtasks/',headers={'Authorization': ('Token {0}'.format(token))},data = payload)
        p4 = json.loads(p4_json.content)
        print p4
    except Exception as e:
        print e


def post_data():
    try:
        token = '1a5367f62221575fdd35921f2364d18f551a8501'
        payload = {'operater':'hugo_16','message':'16'}
        p4_json=requests.post('http://127.0.0.1:10000/mission/dread/',headers={'Authorization': ('Token {0}'.format(token))},data = payload)
        p4 = json.loads(p4_json.content)
        print p4
    except Exception as e:
        print e

from framework import tasks
def input_mysql():
    in_data = tasks.get_redis_queue.delay()
    print in_data

# test_token()
# test_p2()
# test_p3()
# test_data()
post_data()
input_mysql()
# get_data()
# d_data()