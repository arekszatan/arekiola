from django.shortcuts import render
from rest_framework.authentication import TokenAuthentication
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from .models import ColorDb
from .serializer import ColorDbSerializer


def index(request):
    return render(request, 'index.html')


class NameColorText(APIView):
    authentication_classes = (TokenAuthentication,)

    def get(self, request, *args, **kwargs):
        color_list = ColorDb.objects.all()
        serializer = ColorDbSerializer(color_list, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)

    def post(self, request, *args, **kwargs):
        obj = ColorDb.objects.get(name=request.data.get('name'))
        obj.textColor = request.data.get('textColor')
        obj.save()
        color_list = ColorDb.objects.all()
        serializer = ColorDbSerializer(color_list, many=True)
        return Response(serializer.data, status=status.HTTP_201_CREATED)
