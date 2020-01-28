"""crd content
cd likes
content share request
previews"""
from rest_framework.permissions import IsAuthenticated
from django.views import View
from django.conf import settings
from .serializers import *
from account.models import User
from moji.permissions import *
from django.http import JsonResponse
from rest_framework.authtoken.views import ObtainAuthToken
from rest_framework.authtoken.models import Token
from rest_framework.response import Response
from rest_framework.authentication import TokenAuthentication
from django.contrib.auth import authenticate
from rest_framework.decorators import api_view, authentication_classes, permission_classes


def verify_following(f_user_following,c_user):
    return f_user.profile.following.filter(user=c_user).exists()


@api_view(['POST'])
@permission_classes([IsAuthenticated])
def create_comment(request,uuid):
    serializer = CommentSerializer(data=request.data)
    if serializer.is_valid():
        content = Content.objects.get(uuid=uuid)
        if settings.verify_following(request.user,content.user):
            Comment.objects.create(content=content, user=request.user **serializer.validated_data)
            return Response({'outcome':'success'})
        else:
            return Response({'outcome':'user not following c_user'})
    return Response({'outcome':'error'})
    #check if user in following

#DONE
@api_view(['GET'])
def get_content_comments(request,uuid):
    if request.method == "GET":
        parent = Content.objects.get(uuid=uuid)
        if verify_following(request.user,parent.user):
            comments= Comment.objects.filter(ParentContent=parent)
            serializer = CommentsSerializer(comments,many=True)
            if serializer.is_valid():
                return Response({'outcome':serializer.validated_data})
            else:
                return Response({'outcome':'error'})
        else:
            return Response({'outcome':'user not following c_user'})

@api_view(['POST'])
def create_content(request):
    if request.method == "POST":
        serializer = CreateContentSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save(user=request.user)
            return Response({'outcome':'success'})
        return Response({'outcome':'failed'})
#DONE
@api_view(['POST'])
def delete_comment(request):
    if request.method == "POST":
        serializer = UUIDSerializer(data=request.data)
        if serializer.is_valid():
            try:
                a = Comment.objects.get(uuid=serializer.validated_data['uuid'],user=request.user)
            except Comment.DoesNotExist:
                return Response({'outcome':'unauthed request'})
            a.delete()
            return Response({'outcome':'success'})

#DONE
@api_view(['GET'])
@permission_classes([])
def get_content_detail(request,uuid):
    if request.method ==  "GET":
        try:
            a = Content.objects.get(uuid=uuid)
        except Content.DoesNotExist:
            return Response({'outcome':404})
        #if request.user.profile.following.filter(user=a.user.profile).exists():
        ser1 = ContentFrameSerializer(a, context={'user':request.user})
        if a.typeContent=='post':
            ser2 = PostSerializer(a.content_data)
        elif a.typeContent=='video':
            ser2 = VideoSerializer(a.content_data)
        else:
            ser2 = QPostSerializer(a.content_data)
        return Response({'outcome':'success', 'content_frame':ser1.data, 'content_data':ser2.data})

#DONE
@api_view(['POST'])
def delete_content(request):
    if request.method == "POST":
        serializer = UUIDSerializer(data=request.data)
        if serializer.is_valid():
            try:
                a = Content.objects.get(uuid=serializer.validated_data['uuid'], user=request.user)
            except Content.DoesNotExist:
                return Response({'outcome':'unauthed request'})
                a.delete()
                return Response({'outcome':'content deleted'})

#DONE
@api_view(['POST'])
def send_content_share(request):
    if request.method == "POST":
        serializer =  ContentShareRequestSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response({'outcome':'success'})
        else:
            return Response({'outcome':'error'})

#DONE
@api_view(['POST'])
def manage_content_share(request):
    if request.method == "POST":
        serializer = ContentShareManageSerializer(data=request.data)
        if serializer.is_valid():
            req = ContentShareRequest.objects.get(uuid=serializer.validated_data['uuid'])
            if request.user == req.userTo:
                if serializer.validated_data['action'] == 'ACCEPT':
                    req.accept = True
                    req.save()
                elif serializer.validated_data['action'] == 'DENIED':
                    req.delete()
                return Response({'outcome':'passed'})
            else:
                return Response({'outcome':'unauth request'})

def update_likes(request):
    #likes get sent to a redis node and update content likes every x interval if new likes exists
    pass
