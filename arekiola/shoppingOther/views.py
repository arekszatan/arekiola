from django.shortcuts import render
from rest_framework.authentication import TokenAuthentication
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from .models import ShoppingOtherDb
from .serializer import ShoppingOtherSerializer


def index(request):
    return render(request, 'index.html')


class ShoppingOtherRemove(APIView):
    authentication_classes = (TokenAuthentication,)

    def post(self, request, *args, **kwargs):
        ShoppingOtherDb.objects.get(pk=request.data.get('id')).delete()
        shopping_other_item = ShoppingOtherDb.objects.all()
        serializer = ShoppingOtherSerializer(shopping_other_item, many=True)
        return Response(serializer.data, status=status.HTTP_201_CREATED)


class ShoppingOtherUpdate(APIView):
    authentication_classes = (TokenAuthentication,)

    def post(self, request, *args, **kwargs):
        print(request.data)
        obj = ShoppingOtherDb.objects.get(pk=request.data.get('id'))
        obj.product = request.data.get('product')
        obj.done = request.data.get('done')
        obj.save()
        list_shopping_other = ShoppingOtherDb.objects.all()
        serializer = ShoppingOtherSerializer(list_shopping_other, many=True)
        return Response(serializer.data, status=status.HTTP_201_CREATED)


class ShoppingOtherView(APIView):
    authentication_classes = (TokenAuthentication,)

    def get(self, request, *args, **kwargs):
        list_shopping_other = ShoppingOtherDb.objects.all()
        serializer = ShoppingOtherSerializer(list_shopping_other, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)

    def post(self, request, *args, **kwargs):
        if request.data.get('id') is None:
            data = {
                'product': request.data.get('product'),
                'done': request.data.get('done')
            }
            serializer = ShoppingOtherSerializer(data=data)
            if serializer.is_valid():
                serializer.save()
                return Response(serializer.data, status=status.HTTP_201_CREATED)

            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
        else:
            ShoppingOtherDb.objects.get(pk=request.data.get('id')).delete()

