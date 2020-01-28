import re
from rest_framework.response import Response
from django.conf import settings
from django.urls import reverse
from django.shortcuts import redirect
from django.contrib.auth import logout
from rest_framework.decorators import api_view, authentication_classes, permission_classes

class CorsMiddleware(object):
    def __init__(self, get_response):
        self.get_response = get_response

    def __call__(self, request):
        response = self.get_response(request)
        response["Access-Control-Allow-Origin"] = "*"

        return response

AUTH_URLS = [re.compile(settings.AUTH_URL.lstrip('/'))]
if hasattr(settings, 'AUTH_REQUIRED_URLS'):
    AUTH_URLS += [re.compile(url) for url in settings.AUTH_REQUIRED_URLS]

POPUP_URLS = []#[re.compile(settings.LOGIN_URL.lstrip('/'))]
if hasattr(settings, 'SUB_POPUP_URLS'):
    POPUP_URLS += [re.compile(url) for url in settings.SUB_POPUP_URLS]

class AuthRequiredMiddleware:

    def __init__(self, get_response):
        self.get_response = get_response

    def __call__(self, request):
        response = self.get_response(request)
        return response

    def process_view(self, request, view_func, view_args, view_kwargs):
        assert hasattr(request, 'user')
        path = request.path_info.lstrip('/')
        auth_needed_urls = any(url.match(path) for url in AUTH_URLS)
        #url_is_popup = any(url.match(path) for url in POPUP_URLS)
        #if path == reverse('account:logout').lstrip('/'):
        #    logout(request)
        if not request.user.is_authenticated() and auth_needed_urls:
            return redirect('account:unauthed')
        else:
            return None
"""        elif request.user.is_authenticated() or url_is_exempt:
            return None #redirect('home:home')
        else:
            return redirect('account:login')"""

class BlockedMiddleware:

    def __init__(self, get_response):
        self.get_response = get_response

    def __call__(self, request):
        response = self.get_response(request)
        return response

    def process_view(self, request, view_func, view_args, view_kwargs):
        assert hasattr(request, 'user')
        path = request.path_info.lstrip('/')
        #cover these urls profile view, comment, content detail, requests creation,
        if path == reverse('content:detail').lstrip('/'):
            content = Content.objects.get(id=name)
        else:
            user = User.objects.get(username=name)

        Currentpath = any(url.match(path) for url in settings.BLOCKED_URLS)
        #this should cover the profile, content of the user, requests
        #add a blocked clause so the user cant access their content or try to follow them again
        if Currentpath:
            if request.user in user.profile.blocked.all():
                return redirect('account:blockedby')
            elif content.user in request.user.profile.blocked.all():
                return redirect('account:ownerblocked')
            else:
                return None
        else:
            return None

class PageNotFoundMiddleware:

    def __init__(self, get_response):
        self.get_response = get_response

    def __call__(self, request):
        response = self.get_response(request)
        return response

    def process_view(self, request, view_func, view_args, view_kwargs):
        assert hasattr(request, 'user')
        path = request.path_info.lstrip('/')
        #cover these urls profile view, comment, content detail, requests creation,
        if path == reverse('content:detail').lstrip('/'):
            content = Content.objects.get(id=name)
        else:
            user = User.objects.get(username=name)




class AuthenticationRequired:
    pass
