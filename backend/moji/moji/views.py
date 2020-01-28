from django.views import View
from django.shortcuts import render, redirect, Http404
from content.serializers import *
from rest_framework.authtoken.models import Token
from rest_framework.response import Response
from rest_framework.authentication import TokenAuthentication
from django.contrib.auth import authenticate
from rest_framework.decorators import api_view, authentication_classes

def home(request):
    return render(request, 'pages/moji/home.html')

@api_view(['GET'])
def feed(request):
    if request.method == "GET":
        ser = FeedContentSerializer(request.user.feed.payloads.all(), many=True)
        return Response({'outcome':'success','data':ser.data})

def profile(request):
    con = request.user.content.all()
    ser = ProfileContentSerializer(con,many=True)
