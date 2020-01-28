from django.views import View
from django.conf import settings
from .serializers import *
from .models import *
from django.http import JsonResponse
from rest_framework.authtoken.views import ObtainAuthToken
from rest_framework.authtoken.models import Token
from rest_framework.response import Response
from rest_framework.authentication import TokenAuthentication
from rest_framework.permissions import IsAuthenticated
from django.contrib.auth import authenticate
from rest_framework.decorators import api_view, authentication_classes, permission_classes, parser_classes
from rest_framework.parsers import JSONParser, MultiPartParser
from django.contrib.auth.views import  logout
from moji.project_funcs import *
from django.http import HttpResponse
#follow users
#crud following

@api_view(['GET'])
def unauthed(request):
    return Response({'outcome':'unauthed request'})


@api_view(['POST','PUT'])
@permission_classes([])
#@parser_classes([JSONParser, MultiPartParser])
def postFile(request):
    if request.method in ['POST','PUT']:
        ser = FileSer(data=request.data)
        if ser.is_valid():
            upload_handler_chunk(ser.validated_data['file'])
            return Response({'outcome':'success', 'data':ser.validated_data['file'].name})
        return Response({'outcome':ser.errors})

@api_view(['POST'])
@permission_classes([])
def send_lastSeen(request):
    if request.method =="POST":
        if not request.user.is_authenticated():
            return Response({"outcome":'error'})
        serializer = LastSeenSerializer(data=request.data)
        if serializer.is_valid():
            LastSeen.objects.create(ip_of_seen=serializer.validated_data['ip_of_seen'],user=request.user)
            return Response({'outcome':'success'})
        else:
            return Response({'outcome':'retry'})

@api_view(['POST'])
@permission_classes([])
def authUser(request):
    #add logout if using sessions with api
    if request.method == "POST":
        #print(request.data)
        serializer = UserLoginSerializer(data=request.data)
        if serializer.is_valid():
            user = authenticate(**serializer.validated_data)
            if user is not None:
                token, created = Token.objects.get_or_create(user=user)
                return Response({'token':token.key, 'outcome':'success'})
            else:
                return Response({'outcome':'failure to authorize','error':user})
        else:
            return Response({'outcome':'error with data', 'errors':serializer.errors})

@api_view(['POST'])
@permission_classes([])
def create_user_and_profile(request):
    if request.method == "POST":
        serializer = UserCreateSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response({'outcome':'success'})
        else:
            return Response({'outcome':'error with data','error':serializer.errors})


@api_view(['POST'])
def block_or_unblock_user(request):
    if request.method == "POST":
        serializer = BlockUserSerializer(request.data)
        if serializer.is_valid():
            try:
                user = User.objects.get(uuid=serializer.validated_data['blocked_user'])
            except User.DoesNotExist:
                return Response({'outcome':'404 user'})
            action = serializer.validated_data['action']
            if user != request.user:
                if action == "BLOCKED":
                    request.user.blocked.add(user)
                    if user in request.user.profile.following:
                        request.user.followed_by.remove(user)
                        request.user.profile.blocked.add(user)
                        return Response({'outcome':'success'})
                elif action == "UNBLOCKED":
                    request.user.blocked.remove(user)
                    return Response({'outcome':'success'})
                else:
                    return Response({'outcome':'unknown error'})
            else:
                return Response({'outcome':'cannot block yourself'})


@api_view(['POST'])
def delete_user_and_profile(request):
    if request.method == "POST":
        serializer = DeleteUserSerializer(data=request.data)
        if serializer.is_valid():
            if serializer.validated_data['password1'] != serializer.validated_data['password2']:
                return Response({'outcome':'passwords do not match'})
            if not request.user.check_password(serializer.validated_data['password1']):
                return Response({'outcome':'password is invalid'})
            request.user.delete()
            return Response({'outcome':'success'})
        else:
            return Response({'outcome':'error with data'})

@api_view(['PUT'])
def update_user_or_profile(request):
    if request.method == "PUT":
        serializer = UserSerializer(request.user, data=request.data, partial=True)
        if serializer.is_valid():
            serializer.save()
            return Response({'outcome':'success', 'data':request.data, 'sdata':serializer.validated_data})
        return Response({'outcome':'error with data'})


@api_view(['GET'])
@permission_classes([])
def get_user_and_profile_with_content(request, username):
    if request.method == "GET":
        if not request.user.is_authenticated():
            user = User.objects.get(username=username)
            serializer = UserProfileContentSerializer({'user':user,'profile':user.profile,'content':user.content_set.all()})
            return Response({'outcome':'success','data':serializer.data})
        else:
            if username == request.user.username:#check for lower() if raises issue
                serializer = UserProfileContentSerializer({'user':request.user,'profile':request.user.profile,'content':request.user.content_set.all()})
                return Response({'outcome':'success','data':serializer.data})
            else:
                try:
                    user = User.objects.get(username=username)
                except User.DoesNotExist:
                    return Response({'outcome':'404 user'})
                if verify_following(request.user,user.uuid):
                    serializer = UserProfileContentSerializer({'user':user,'profile':user.profile,'content':user.content_set.all()})
                else:
                    serializer = UserProfileContentSerializer({'user':user,'profile':user.profile,'content':user.content_set.filter(preview=True)})
                return Response({'outcome':'success', 'data':serializer.data})



@api_view(['POST'])
def change_user_password(request):
    if request.method == "POST":
        serializer = PasswordChangeSerializer(request.data)
        if serializer.is_valid():
            #user = request.user
            if not request.user.check_password(serializer.validated_data['old_password']):
                return Response({'outcome':'password is invalid'})
            if serializer.validated_data['new_password1'] != serializer.validated_data['new_password2']:
                return Response({'outcome':'confirmation password does not match new password'})
                #should handle on frontend
            request.user.set_password(serializer.validated_data['new_password1'])
            request.user.save()
            return Response({'outcome':'success'})


@api_view(['GET'])
def get_following(request):
    if request.method == "GET":
        ser = UserNoAccountSerializer(request.user.profile.following, many=True)
        return Response({'outcome':ser.validated_data})

@api_view(['GET'])
def get_followers(request):
    if request.method == "GET":
        serializer = UserNoAccountSerializer(request.user.profile.following,many=True)
        if serializer.is_valid():
            return Respone({'outcome':'success','results':serializer.validated_data})

@api_view(['POST'])
def remove_follower(request):
    if request.method == "POST":
        serializer = UUIDSerializer(data=request.data)
        if serializer.is_valid():
            i_user = User.objects.get(uuid=serializer.validated_data['uuid'])
            request.user.following.remove(i_user.profile)
            return Response({'outcome':'success'})
        else:
            return Response({'outcome':'error with data'})

"""
@api_view(['POST'])
def send_follow_request(request):
    if request.method == "POST":
        serializer = UUIDSerializer(data=request.data)
        if serializer.is_valid():
            user = User.objects.get(uuid=serializer.validated_data['uuid'])
            #passing a user object
            AccountRequest.objects.create(userTo=)
            return Response({'outcome':'success'})

@api_view(['GET'])
def get_all_follow_requests(request):
    if request.method == "GET":
        serializer = AllFollowRequestSerializer(request.user.requested.all(),many=True)
        #if serializer.is_valid():
        return Response({'outcome':serializer.data})

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

@api_view(['POST'])
def unsend_follow_request(request):
    if request.method == "POST":
        serializer = UUIDSerializer(data=request.data)
        if serializer.is_valid():
            try:
                #handles if request.user is the one who sent the request
                req =  AccountRequest.objects.filter(userFrom=request.user).get(uuid=serializer.validated_data['uuid'])
            except AccountRequest.DoesNotExist:
                return Response({'outcome':'can not find follow request'})
            req.delete()
            return Response({'outcome':'success'})

"""














































"""from django.shortcuts import render, redirect
from account.models import Profile, AccountRequest
from content.models import Content
from django.urls import reverse
from django.contrib.auth.models import User
from django.contrib.auth import update_session_auth_hash
from django.http import Http404
from .forms import RegistrationForm, EditProfileForm, UpdateUserForm, RequestForm
from django.contrib.auth.forms import PasswordChangeForm
from django.views import View

#ACCOUNT SUITE

def blockUser(request, uuid=None):
    try:
        user = User.objects.get(uuid=uuid)
    except User.DoesNotExist():
        raise Http404("User does not exist")
    if user == request.user:
        return None
        return redirect(reverse('home:home'))
    elif user in request.user.profile.following:
        request.user.profile.following.remove(user)
        request.user.followed_by.remove(user)
        request.user.profile.blocked.add(user)
        return redirect(reverse('home:home'))
    else:
        request.user.profile.blocked.add(user)
        return redirect(reverse('home:home'))
    #take the user and current user,
    #1. blocked the user by adding to blocked list
    #2. remove user from following

def unblockUser(request, uuid=None):
    try:
        user = User.objects.get(uuid=uuid)
    except User.DoesNotExist():
        raise Http404("User does not exist")
    request.user.profile.blocked.remove(user)
    return redirect(reverse('home:home'))

def ViewProfile(request, name=None):
    try:
        user = User.objects.get(username=name)
    except User.DoesNotExist:
        raise Http404("User does not exist")
    if request.user.is_authenticated() == False:
        return render(request, "pages/1/privateprofile.html", {"user":user, 'unauthed':True})
    elif name == request.user.username:
        return render(request, "pages/1/ownerprofile.html", {"user":user})
    elif user.profile.private and user not in request.user.profile.following.all():
        return render(request, "pages/1/privateprofile.html", {"user":user})
    else:
        return render(request, "pages/1/viewprofile.html", {"user":user})

def updateProfile(request):
    if request.method  == "POST":
        form = EditProfileForm(request.POST, instance=request.user)
        form1 = UpdateUserForm(request.POST, request.FILES, instance=request.user.profile)
        if form.is_valid() and form1.is_valid():
            #profile = form.save(commit=False)
            #profile.first_name = form.cleaned_data['first_name']
            #profile.last_name = form.cleaned_data['last_name']
            #profile.email = form.cleaned_data['email']
            form.save()
            form1.save()
            return redirect(reverse('account:ProfileView', kwargs={'name':request.user.username}))
        else:
            #messages.error(request, "Error")
            return render(request, 'pages/2/signup.html', {'form':form})

    else:
        form = EditProfileForm(instance=request.user)
        form1 = UpdateUserForm(instance=request.user.profile)
        return render(request, 'pages/5/editprofile.html', {'form':form, 'form1':form1})

def register(request):
    if request.method == 'POST':
        form = RegistrationForm(request.POST)
        if form.is_valid():
            form.save()
            '''reg = form.save(commit=False)
            reg.email = form.cleaned_data['email']
            reg.username = form.cleaned_data['username']
            reg.first_name = form.cleaned_data['first_name']
            reg.last_name = form.cleaned_data['last_name']
            reg.password1 = form.cleaned_data['password1']
            reg.password2 = form.cleaned_data['password2']

            reg.save()'''
            return redirect(reverse('account:login'))

        else:
            #messages.error(request, "Error")
            return render(request, 'pages/2/signup.html', {'form':form})

    else:
        form = RegistrationForm()
        return render(request, 'pages/2/signup.html', {'form':form})

def deleteProfile(request):
    #add a re-enter passcode to delete account
    user = User.objects.get(uuid=request.user.uuid)
    user.delete()
    return redirect('/home')

def change_password(request):
    if request.method == 'POST':
        form = PasswordChangeForm(data=request.POST, user=request.user)

        if form.is_valid():
            form.save()
            update_session_auth_hash(request, form.user)
            return redirect(reverse('content:CreatePost'))
        else:
            return redirect(reverse('account:change_password'))
    else:
        form = PasswordChangeForm(user=request.user)

        args = {'form': form}
        return render(request, 'account/password.html', args)


#PREVIEW SUITE
'''method 1, on content list a add to preview link is there and sends the id of the content to this url and adds as a preview,
and vise versa when they want to remove.
'''

def previewRemoveAdd(request, uuid=None):
    #print(str(uuid))
    try:
        content = Content.objects.get(uuid=uuid)
    except User.DoesNotExist():
        raise Http404("User does not exist")
    if content.user == request.user and content.preview == False:
        content.preview = True
        content.save()
        return redirect(reverse('account:ProfileView', kwargs={'name':request.user.username}))
    elif content.user == request.user and content.preview == True:
        content.preview = False
        content.save()
        return redirect(reverse('account:ProfileView', kwargs={'name':request.user.username}))
    else:
        return redirect(reverse('home:home'))




#FOLLOW SUITE

def listRequests(request):
    return render(request, 'pages/lists/requestlist.html')

def detailRequests(request, name):
    try:
        user = User.objects.get(username=name)
        req = request.user.requested.get(userFrom=user)
        #req = AccountRequest.objects.filter(userFrom=request.user).get(userTo=name)
    except AccountRequest.DoesNotExist:
        raise Http404("Cant find that request")
    return render(request, 'account/reqDetail.html', {'req':req})

def deleteRequests(request, name):
    try:
        user = User.objects.get(username=name)
        req = request.user.requested.get(userFrom=user)
        #req = AccountRequest.objects.filter(userFrom=request.user).get(userTo=name)
        req.delete()
    except AccountRequest.DoesNotExist:
        raise Http404("Cant find that request")
    return redirect(reverse('account:ProfileView', kwargs={'name':request.user.username}))

def editRequests(request, name):
    try:
        user = User.objects.get(username=name)
        req = request.user.requested.get(userFrom=user)
        #req = AccountRequest.objects.filter(userFrom=request.user).get(userTo=name)
        req.accept = True
        req.save()
    except AccountRequest.DoesNotExist:
        raise Http404("Cant find that request")
    return redirect(reverse('account:ProfileView', kwargs={'name':request.user.username}))

def makeRequests(request, name):
    #need to add where one model can be made, probably use the sent field
    try:
        user = User.objects.get(username=name)
    except AccountRequest.DoesNotExist:
        raise Http404("Cant find that request")
    if AccountRequest.objects.filter(userFrom=request.user).get(userTo=user).exists():
        return None
    else:
        accept = AccountRequest()
        accept.userTo = user
        accept.userFrom = request.user
        accept.save()
        return redirect(reverse('account:ProfileView', kwargs={'name':request.user.username}))

def unfollowUser(request, name):
    try:
        user = User.objects.get(username=name)
        request.user.profile.following.remove(user)
        #req = AccountRequest.objects.filter(userFrom=request.user).get(userTo=name)
    except AccountRequest.DoesNotExist:
        raise Http404("Cant find that user")
    return redirect(reverse('home:home'))
"""
