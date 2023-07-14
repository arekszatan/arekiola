from django.shortcuts import render
from rest_framework.authentication import TokenAuthentication
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from .models import ShoppingDb
from .serializer import ShoppingSerializer


def index(request):
    return render(request, 'index.html')


class RemoveRow(APIView):
    authentication_classes = (TokenAuthentication,)

    def post(self, request, *args, **kwargs):
        print(request.data.get('id'))
        ShoppingDb.objects.get(pk=request.data.get('id')).delete()
        todos = ShoppingDb.objects.all()
        serializer = ShoppingSerializer(todos, many=True)
        return Response(serializer.data, status=status.HTTP_201_CREATED)


class UpdateRow(APIView):
    authentication_classes = (TokenAuthentication,)

    def post(self, request, *args, **kwargs):
        print(request.data)
        obj = ShoppingDb.objects.get(pk=request.data.get('id'))
        obj.product = request.data.get('product')
        obj.done = request.data.get('done')
        obj.save()
        list_shopping = ShoppingDb.objects.all()
        serializer = ShoppingSerializer(list_shopping, many=True)
        return Response(serializer.data, status=status.HTTP_201_CREATED)


class TodoListApiView(APIView):
    authentication_classes = (TokenAuthentication,)

    def get(self, request, *args, **kwargs):
        list_shopping = ShoppingDb.objects.all()
        serializer = ShoppingSerializer(list_shopping, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)

    def post(self, request, *args, **kwargs):
        if request.data.get('id') is None:
            data = {
                # 'id': request.data.get('id'),
                'product': request.data.get('product'),
                'done': request.data.get('done')
            }
            serializer = ShoppingSerializer(data=data)
            if serializer.is_valid():
                serializer.save()
                return Response(serializer.data, status=status.HTTP_201_CREATED)

            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
        else:
            ShoppingDb.objects.get(pk=request.data.get('id')).delete()

