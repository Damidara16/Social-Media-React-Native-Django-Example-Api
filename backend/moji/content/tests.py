from django.test import TestCase, tag
from .models import *
from account.models import User
from rest_framework.authtoken.models import Token
from rest_framework.test import APIClient

def create_pre_user(number):
    name  = 'test' + str(number)
    user = User.objects.create(username=name, email=name+'@test.com',date_of_birth='2000-12-12')
    user.set_password('pass1234')
    user.save()
    Token.objects.get_or_create(user=user)
    return user

def create_content(user):
    con = Content.objects.create(typeContent="qpost", user=user)
    qp = QPost.objects.create(content_meta=con, qpost='hello world')
    return qp

class feed_TestCase(TestCase):
    def setUp(self):
        a = create_pre_user(1)
        b = create_pre_user(2)
        c = create_pre_user(3)
        a.followed_by.add(b.profile)
        a.followed_by.add(c.profile)

    def test_expected_success(self):
        user = User.objects.get(username='test1')
        user2 = User.objects.get(username='test2')
        user3 = User.objects.get(username='test3')
        create_content(user)
        f = FeedObject.objects.first()
        self.assertIn(f, user2.feed.payloads.all())
        self.assertIn(f, user3.feed.payloads.all())

@tag('detail')
class detail_TestCase(TestCase):
    cli = APIClient()
    def setUp(self):
        user = create_pre_user(1)
        create_content(user)

    def test_expected_success(self):
        c = Content.objects.all()[0]
        u = User.objects.all()[0]
        self.cli.force_authenticate(user=u)
        res = self.cli.get('/content/detail/'+str(c.uuid)+'/')
        print(res.data)
