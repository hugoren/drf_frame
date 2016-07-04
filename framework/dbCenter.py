#coding:utf-8

from rest_framework.decorators import api_view, permission_classes
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from rest_framework.views import APIView


@api_view(['POST',])
@permission_classes([IsAuthenticated, ])
def dr(req):
    operater,message,app,other = None,None,None,None
    try:
        if req.method == 'POST':
            operater = req.POST.get('operater')
            log_dict = {'operater':operater}
            return Response(log_dict)
        else:
            return Response('只接受post请求')
    except Exception as e:
        return  Response(e.message)


class DBREAD(APIView):
    permission_classes = (IsAuthenticated,)


    def post(self, req, format=None):

        operater,message,app,other = None,None,None,None
        try:
            if req.method == 'POST':
                operater = req.POST.get('operater')
                log_dict = {'operater':operater}
                return Response(log_dict)
            else:
                return Response('只接受post请求')
        except Exception as e:
            return Response(e.message)
