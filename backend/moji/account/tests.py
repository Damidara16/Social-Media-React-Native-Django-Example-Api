from django.test import TestCase, tag
from .models import *
from rest_framework.authtoken.models import Token
from rest_framework.test import APIClient

#NAMING ERROR client IS A RESERVED WORD
def create_pre_user(number):
    name  = 'test' + str(number)
    user = User.objects.create(username=name, email=name+'@test.com',date_of_birth='2000-12-12')
    user.set_password('pass1234')
    user.save()
    Token.objects.get_or_create(user=user)
    return user

@tag('login')
class login_TestCase(TestCase):
    cli = APIClient()
    test_url = '/account/auth/'

    def setUp(self):
        name  = 'test' + str(1)
        user = User.objects.create(username=name, email=name+'@test.com',date_of_birth='2000-12-12')
        user.set_password('pass1234')
        user.save()
        Token.objects.get_or_create(user=user)
        return user

    def test_response_success(self):
        user = User.objects.get(username='test1')
        self.cli.force_authenticate(user=None)
        res = self.client.post(self.test_url, {'email':user.email,'password':'pass1234'} ,format='json')
        self.assertEqual(res.status_code,200)
        self.assertEqual(res.data['token'],user.auth_token.key)
        self.assertEqual(res.data['outcome'],'success')


@tag('profile')
class get_user_and_profile_with_content_TestCase(TestCase):
    cli = APIClient()
    test_url = '/account/get/user/'

    def setUp(self):
        create_pre_user(1)
        create_pre_user(2)

    def test_response_success(self):
        user = User.objects.get(username='test1')
        user2 = User.objects.get(username='test2')
        user.profile.following.add(user2)
        self.cli.credentials(HTTP_AUTHORIZATION='Token ' + user.auth_token.key)
        res = self.cli.get(self.test_url+'test2/')
        self.assertEqual(res.status_code,200)
        self.assertEqual(res.data['outcome'],'success')


@tag('g_f')
class get_following_TestCase(TestCase):
    test_url = '/account/get/following/'
    cli = APIClient()
    def setUp(self):
        create_pre_user(1)
        create_pre_user(2)

    def test_response_success(self):
        user = User.objects.get(username='test1')
        self.cli.credentials(HTTP_AUTHORIZATION='Token ' + user.auth_token.key)
        res = self.cli.get(self.test_url)
        self.assertEqual(res.status_code,200)
        self.assertEqual(res.data['outcome'],'success')
