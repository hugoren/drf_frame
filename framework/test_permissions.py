#coding:utf-8

from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework.decorators import api_view, permission_classes
from django.views.decorators.csrf import csrf_exempt

import simplejson as json



class permission1(APIView):
    permission_classes = (IsAuthenticated,)

    def get(self, request, format=None):
        content = {
            'status': 'request was permitted'
        }
        return Response(content)

    # def post(self,request,format=None):
    #     data = request.data
    #     print data





@api_view(['GET','POST',])
@permission_classes([IsAuthenticated, ])
def permission2(req,format=None):

    if req.method == 'GET':
        content = {
            'status': ' get  was permitted'
        }
        return Response(content)

    elif req.method == 'POST':
        ii = req.POST.get('app_name')
        data = req.data
        # stream = json.loads(data)
        # print stream
        print ii
        print data
        content = {
            'status': 'post was permitted'
        }
        return Response(content)

    else:
        print None





