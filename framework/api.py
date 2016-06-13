from rest_framework.views import APIView
from rest_framework import status
from framework.models import BOOK
from rest_framework.response import Response
from framework.serializer import BookSerializer


class API(APIView):

    def bookApi(self,request):
        try:
            queryset = BOOK.objects.all()
            print queryset['author']
        except Exception as e:
            return Response(status=status.HTTP_404_NOT_FOUND)

        if request.method == 'GET':
            serializer = BookSerializer(queryset)
            return Response(serializer.data)

        elif request.method == 'POST':
            serializer = BookSerializer(data=request.DATA)
            if serializer.is_valid():
                serializer.save()
                return Response(serializer.data,status=status.HTTP_201_CREATED)
            else:
                return Response(serializer.errors,status=status.HTTP_400_BAD_REQUEST)

        elif request.method == 'PUT':
            serializer = BookSerializer(BOOK,data=request.DATA)
            if serializer.is_valid():
                serializer.save()
                return Response(serializer.data)
            else:
                return Response(serializer.errors,status=status.HTTP_400_BAD_REQUEST)

        elif request.method == 'DELETE':
            BOOK.delete()
            return Response(status=status.HTTP_204_NO_CONTENT)
        elif request.method == 'UPDATE':
            pass
        else:
            pass