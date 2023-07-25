from django.shortcuts import render
from rest_framework.authentication import TokenAuthentication
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
# from .models import ColorDb
# from .serializer import ColorDbSerializer


def index(request):
    return render(request, 'index.html')
