from rest_framework import serializers
#from django.contrib.auth.models import User
from django.conf import settings
from .models import *

class UserContentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Content
        fields = ("__all__")

        #disabled model creation with this serializer
    def create(self,validated_data):
        return None

class CreateContentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Content
        exclude = ("user","uuid","views","date")


class ContentShareRequestSerializer(serializers.ModelSerializer):
    class Meta:
        model = ContentShareRequest
        fields = ("userTo","userFrom","content")


"""class ContentShareManageSerializer(serializers.Serializer):
    #EXPECTED ACTIONS 'ACCEPT' OR 'DENIED'
    action = serializers.CharField(max_length=6)
    uuid = UUIDSerializer()"""

class FeedContentSerializer(serializers.ModelSerializer):
    class Meta:
        model = FeedObject
        fields = ('cuuid','type',)

class VideoSerializer(serializers.ModelSerializer):
    class Meta:
        model = Video
        exclude = ('id','content_meta',)

class PostSerializer(serializers.ModelSerializer):
    class Meta:
        model = Post
        exclude = ('id','content_meta',)

class QPostSerializer(serializers.ModelSerializer):
    class Meta:
        model = QPost
        exclude = ('id','content_meta',)

"""
      <FlatList
        data={this.data}
        keyExtractor={(item, index) => index.toString()}
        renderItem={ ({ item , index }) => {
          <View style={{height:20, width:'100%',backgroundColor:'red'}}></View>

        }}
      />
       switch (item.type) {
          case 'post':
            <Poster uuid={item.cuuid}/>
            break;
          case 'tweet':
            <Tweeter uuid={item.cuuid}/>
            break;
          case 'image':
            <Imager uuid={item.cuuid}/>
            break;
        }
"""


class ContentFrameSerializer(serializers.ModelSerializer):
    liked = serializers.SerializerMethodField(method_name='get_liked')
    saved = serializers.SerializerMethodField(method_name='get_saved')
    picLink = serializers.URLField(source='user.profile.pic')
    uname = serializers.CharField(source='user.username')
    numLikes = serializers.IntegerField(source='likes')
    date = serializers.DateTimeField(format="%Y/%m/%d %H:%M:%S")
    class Meta:
        model = Content
        fields = ('uuid','numLikes', 'date', 'liked', 'saved' ,'numComs', 'picLink', 'uname')

    def get_saved(self,obj):
        user = self.context.get('user')
        return user.bookmarks.payloads.filter(cuuid=obj.uuid).exists()

    def get_liked(self, obj):
        user = self.context.get('user')
        return obj.like_set.filter(user=user).exists()

class ProfileContentSerializer(serializers.Serializer):
    content = ContentFrameSerializer()
    qp_data = QPostSerializer(required=False)
