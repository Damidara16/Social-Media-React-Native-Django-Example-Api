from rest_framework import serializers
from django.conf import settings
from .models import *
from content.serializers import UserContentSerializer
#there may be a problem with UserSerialzer with password field and get non owner accounts
#needed for account updates,creations, and return account info
class AccountSerializer(serializers.ModelSerializer):
    class Meta:
        model = Profile
        exclude = ("user",)

class UserCreateSerializer(serializers.ModelSerializer):
    profile = AccountSerializer(required=False)
    class Meta:
        model = User
        fields = ("date_of_birth","email","username","password","profile")


    def create(self,validated_data):
        if validated_data.get('profile'):
            p_data = validated_data.pop('profile')
        #password = validated_data.pop(['password'])
        user = User.objects.create(**validated_data)
        if validated_data.get('profile'):
            Profile.objects.create(user=user,**p_data)
        return user

"""class UsersProfileContentSerializer(serializers.Serializer):
    profile = AccountSerializer()
    user = UserSerializer()
    content = UserContentSerializer(many=True)"""


class AllFollowRequestSerializer(serializers.ModelSerializer):
    class Meta:
        model = AccountRequest
        exclude = ("userTo","uuid")

class UserNoAccountSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        exclude = ('password',)


class UserBannerSerializer(serializers.ModelSerializer):
    bio = serializers.CharField(allow_blank=True, allow_null=True, max_length=255, required=False)
    class Meta:
        model = User
        fields = ('username','uuid','bio',)
        #hidden_fields = ('uuid',)

class UserProfileContentSerializer(serializers.Serializer):
    user = UserNoAccountSerializer()
    profile = AccountSerializer()
    content = UserContentSerializer(many=True)

class UserLoginSerializer(serializers.Serializer):
    email = serializers.EmailField()
    password = serializers.CharField()




#used for any model lookup
class UUIDSerializer(serializers.Serializer):
    uuid = serializers.UUIDField(format="hex_verbose")

class LastSeenSerializer(serializers.Serializer):
        ip_of_seen= serializers.IPAddressField(required=True)

class ChoicesField(serializers.Field):
    def __init__(self, choices, **kwargs):
        self._choices = choices
        super(ChoicesField, self).__init__(**kwargs)

    def to_representation(self, obj):
        return self._choices[obj]

    def to_internal_value(self, data):
        return getattr(self._choices, data)



class FollowRequestSerializer(serializers.Serializer):
    #EXPECTED ACTIONS 'ACCEPT' OR 'DENIED'
    action = serializers.CharField(max_length=6)
    userTo_uuid = UUIDSerializer()

class BlockUserSerializer(serializers.Serializer):
    #BUB = (("BLOCKED","BLOCKED"), ("UNBLOCKED","UNBLOCKED"))
    blocked_user = serializers.UUIDField()
    action = serializers.CharField(max_length=9)

class PasswordChangeSerializer(serializers.Serializer):
    old_password = serializers.CharField()
    new_password1 = serializers.CharField()
    new_password2 = serializers.CharField()

class DeleteUserSerializer(serializers.Serializer):
    password1 = serializers.CharField()
    password2 = serializers.CharField()
