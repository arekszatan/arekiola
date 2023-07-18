from django.shortcuts import render
from rest_framework.authentication import TokenAuthentication
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from .models import WalletListDb
from .serializer import WalletListSerializer


def index(request):
    return render(request, 'index.html')


class WalletListDbView(APIView):
    authentication_classes = (TokenAuthentication,)

    def get(self, request, *args, **kwargs):
        wallet_list = WalletListDb.objects.all()
        serializer = WalletListSerializer(wallet_list, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)


class WalletListAddDbView(APIView):
    authentication_classes = (TokenAuthentication,)

    def post(self, request, *args, **kwargs):
        data = {
            'female': request.data.get('female'),
            'person': request.data.get('person'),
            'price': request.data.get('price')
        }
        serializer = WalletListSerializer(data=data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class WalletListRemoveAllDbView(APIView):
    authentication_classes = (TokenAuthentication,)

    def post(self, request, *args, **kwargs):
        WalletListDb.objects.all().delete()
        wallet_list = WalletListDb.objects.all()
        serializer = WalletListSerializer(wallet_list, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)
