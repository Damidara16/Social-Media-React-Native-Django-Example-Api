from django.views import View
from django.conf import AUTH_USER_MODEL
from .serializers import *
from .models import *
from django.http import JsonResponse
from rest_framework.authtoken.views import ObtainAuthToken
from store_user.models import Store
from rest_framework.authtoken.models import Token
from rest_framework.response import Response
from django.contrib.auth import authenticate
from rest_framework.decorators import api_view

#follow users
#crud following

@api_view(['POST'])
def Login(request):
    if request.method == 'POST':
        serializer = UserLoginSerializer(data=request.data)
        if serializer.is_valid():
            user = authenticate(**serializer.validated_data)
            if user is not None:
                token, created = Token.objects.get_or_create(user=user)
                return Response({'token':token.key, 'outcome':'success'})
            else:
                return Response({'outcome':'failure to authorize'})
        else:
            return Response({'outcome':'error 8320, please contact us for more help'})

@api_view(['POST'])
def create_user_and_profile(request):
    if request.method == "POST":
        serializer = UserSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        else:
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


@api_view(['POST'])
def block_or_unblock_user(request):
    if request.method == "POST":
        serializer = BlockUserSerializer(request.data)
        if serializer.is_valid():
            action = serializer.validated_data['action']
            user = User.objects.get(uuid=serializer.validated_data['blocked_user'])
            if user != request.user:
                if action == "BLOCKED":
                    request.user.blocked.add(user)
                    if user in request.user.profile.following:
                        request.user.profile.following.remove(user)
                        request.user.followed_by.remove(user)
                elif action == "UNBLOCKED":
                    request.user.blocked.remove(user)
                else:
                    return Response({'outcome':'unknown error'})
            else:
                return Response({'outcome':'cannot block yourself'})


@api_view(['GET', 'POST'])
def delete_user_and_profile(request):
    if request.method == "":
        pass

@api_view(['PUT'])
def update_user_or_profile(request):
    if request.method == "PUT":
        serializer = UserSerialzer(request.user, data=request.data, partial=True)
        if serializer.is_valid():
            serializer.save()
            return Response({'outcome':'account updated'})
        return Response({'outcome':'unknown error'})


@api_view(['GET'])
def get_user_and_profile(request):
    if request.method == "GET":
        serializer = UUIDSerializer(request.data)
        #just call api with token and returns user
        if not serializer:
            user = UserSerialzer(user=request.user)
            return Response({'outcome':user})
        if serializer.is_valid():
            try:
                user = MODEL.objects.get(uuid=serializer.validated_data['uuid'])
            except User.DoesNotExist:
                return Response({'outcome':'can not find user'})
            user = AccountSerialzer(user=user)
            return Response({'outcome':user})
        else:
            return Response({'outcome':'unknown error'})

@api_view(['POST'])
def change_user_password(request):
    if request.method == "POST":
        serializer = PasswordChangeSerializer(request.data)
        if serializer.is_valid():
            #user = request.user
            if not request.user.check_password(serializer.validated_data['old_password']):
                return Response({'outcome':'password is invalid'})
            if serializer.validated_data['new_password1'] != serializer.validated_data['new_password2']:
                return Response({'outcome':'confirmation password does not match new password '})
                #should handle on frontend
            request.user.set_password(serializer.validated_data['new_password1'])
            request.user.save()
            return Response({'outcome':'password changed'})

@api_view(['POST'])
def send_follow_request(request):
    if request.method == "POST":
        serializer = FollowRequestSerializer(data=request.data)
        if serializer.is_valid():
            #passing a user object
            serializer.save()
            #AccountRequest.objects.create(userTo=)
            return Response({'outcome':'success'})


@api_view(['GET'])
def get_all_follow_requests(request):
    if request.method == "GET":
        serializer = FollowRequestSerializer(data=request.user.AccountRequest.all(),many=True)
        if serializer.is_valid():
            return Response({'outcome':serializer.validatied_data})

@api_view(['POST'])
def manage_follow_request(request):
    if request.method == "POST":
        serializer = FollowRequestSerializer(data=request.data)
        if serializer.is_valid():
            req = AccountRequest.objects.get(uuid=serializer.validated_data['uuid'])
            if request.user == req.userTo:
                if serializer.validated_data['action'] == 'ACCEPT':
                    req.accept = True
                    req.save()
                elif serializer.validated_data['action'] == 'DENIED':
                    req.delete()
                return Response({'outcome':'passed'})
            else:
                return Response({'outcome':'unauth request'})


@api_view(['DELETE'])
def unsend_follow_request(request):
    if request.method == "DELETE":
        serializer = FollowRequestSerializer(data=request.data)
        if serializer.is_valid():
            if request.user == req.userFrom:
                req.delete()
                return Response({'outcome':'success'})

@api_view(['GET'])
def get_following(request):
    if request.method == "GET":
        ser = FollowSerializer(request.user.following, many=True)
        return Response({'outcome':ser})

@api_view(['GET'])
def get_followers(request):
    if request.method == "GET":
        serializer = UserNoAccountSerializer(data=request.user.profile.following,many=True)
        if serializer.is_valid():
            return Respone({'outcome':serializer.validated_data})

@api_view(['POST'])
def remove_follower(request):
    if request.method == "POST":
        serializer = UUIDSerializer(data=request.data)
        if serializer.is_valid():
            i_user = settings.AUTH_USER_MODEL.objects.get(uuid=serializer.vakidated_data['uuid'])
            request.user.following.remove(i_user)
            return Response({'outcome':'sucess'})
