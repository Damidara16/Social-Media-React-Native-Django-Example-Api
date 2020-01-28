from django.db import models
from django.conf import settings
from django.urls import reverse
from account.models import User
import uuid
from django.db.models.signals import pre_delete, post_save


class ContentVideoManager(models.Manager):

    def queryset(self):
        return super(ContentManager, self).get_queryset().filter(typeContent='Video')

class ContentPostManager(models.Manager):

    def queryset(self):
        return super(ContentManager, self).get_queryset().filter(typeContent='Post')

class ContentQPostManager(models.Manager):

    def queryset(self):
        return super(ContentManager, self).get_queryset().filter(typeContent='QPost')


#ACTIVE NOTIF
class Content(models.Model):
    contents = (('post', 'post'),('video', 'video'),('qpost', 'qpost'), ('photo','photo'))#quick post
    uuid = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    date = models.DateTimeField(auto_now_add=True)
    views = models.IntegerField(default=0)
    likes = models.IntegerField(default=0)
    numComs = models.IntegerField(default=0)
    typeContent = models.CharField(max_length=5, choices=contents)
    preview = models.BooleanField(default=False)
    shared = models.BooleanField(default=False)
    follower_sharable = models.BooleanField(default=False) #make seperate model?
    follower_sharable_limit = models.PositiveIntegerField(default=0)
    likesDisabled = models.BooleanField(default=False)
    commentsDisabled = models.BooleanField(default=False)
    #commentLikesDisabled = models.BooleanField(default=False)

    @property
    def content_data(self):
        if self.typeContent=='post':
            return self.p_content_data
        elif self.typeContent=='video':
            return self.v_content_data
        else:
            return self.qp_content_data

    #vid = ContentVideoManager()
    #posted = ContentPostManager()
    #Tweeted = ContentTweetManager()

    def contentToPayload(self):
        pass

    def get_absolute_url(self):
        return reverse('content:detail', kwargs={'uuid':self.uuid})

    def __str__(self):
        return self.typeContent + ' ' + self.user.username

    def commentCount(self):
        if not self.commentsDisabled:
            return self.comment_set.all().count()

    def save(self, *args, **kwargs):
        if not FeedObject.objects.filter(cuuid=self.uuid).exists():
            fObj = FeedObject.objects.create(cuuid=self.uuid)
            for i in self.user.followed_by.all():
                i.user.feed.payloads.add(fObj)
        self.typeContent = self.typeContent.lower()
        super(Content, self).save(*args,**kwargs)

#split the model through forms exclude(), and through views



class Post(models.Model):
    file = models.FileField(null=True,blank=True)
    description = models.CharField(max_length=255)
    caption = models.CharField(max_length=255, null=True)
    content_meta =  models.OneToOneField(Content,related_name='p_content_data')

class Video(models.Model):
    file = models.FileField()
    description = models.CharField(max_length=255)
    caption = models.CharField(max_length=255, null=True)
    content_meta =  models.OneToOneField(Content,related_name='v_content_data')
    thumbnail = models.FileField(null=True, blank=True)

class QPost(models.Model):
    qpost = models.CharField(max_length=200)
    content_meta =  models.OneToOneField(Content,related_name='qp_content_data')


class SubContent(models.Model):
    ParentContent = models.ForeignKey(Content, on_delete=models.CASCADE)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    timeStamp = models.DateTimeField(auto_now_add=True)
    uuid = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)

    class Meta:
        abstract = True

class Comment(SubContent):
    comment = models.CharField(max_length=200)
    likes = models.PositiveIntegerField(default=0)
    #to dislike get the comment uuid and self.likes -= 1
    #comment.save()

    def save(*args, **kwargs):
        self.ParentContent.numCom += 1
        self.ParentContent.save()
        super(Content, self).save(*args,**kwargs)

class CommentLike(models.Model):
    #to get like count on a content, just return the count, there's a function for this called likeCount()
    like = models.BooleanField(default=True)
    ParentComment = models.ForeignKey(Comment, on_delete=models.CASCADE)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    uuid = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False,unique=True)

    def delete(self):
        self.ParentComment.likes -= 1
        super(CommentLike, self).delete()

    def save(self,*args,**kwargs):
        self.ParentComment.likes += 1
        super(CommentLike, self).save(*args,**kwargs)


class ContentShareRequest(models.Model):
    #how to handle n shares
    #user.requested.all() -> gives all the Requested invites and vise-versa
    userTo = models.ForeignKey(settings.AUTH_USER_MODEL, related_name='cs_requested')
    userFrom = models.ForeignKey(settings.AUTH_USER_MODEL, related_name='cs_requester')
    accept = models.BooleanField(default=False)
    content = models.ForeignKey(Content)
    uuid = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False, unique=True)
    #def delete() -> remove_user_uuid
    #ContentShareRequested.objects.get(content=content).usersTo.remove(user)

    def __str__(self):
        return self.userFrom.username

    def get_absolute_url(self):
        return reverse('account:detailAcceptance', kwargs={'name':self.userTo.username})

    def create_confirmed_cs_for_shared_user(self):
        from copy import deepcopy
        content = deepcopy(self.content)
        content.user = self.userTo
        content.pk = None
        content.shared = True
        content.save()

    def save(self, *args, **kwargs):
        #try:
            #a  = ContentShare.objects.get(content=self.content, userTo=self.user)
            #b = Content.objects.get(user=self.userTo, shared_key=self.shared_key)
        #except (ContentShare.DoesNotExist, Content.DoesNotExist):
            #how to handle user mulitple users
            #dont want to create the same content over and over again, lookup saves us money
        if self.accept == True:
            self.create_confirmed_cs_for_shared_user()
            self.content.shared = True
            self.content.save()
            self.delete()
        else:
            super(ContentShareRequest, self).save(*args, **kwargs)


class Like(SubContent):
    #to get like count on a content, just return the count, there's a function for this called likeCount()
    like = models.BooleanField(default=True)

class Playlist(models.Model):
    name = models.CharField(max_length=255, null=True)
    content = models.ManyToManyField(Content)
    creator = models.ForeignKey(User)
    date = models.DateTimeField(auto_now_add=True)
    views = models.IntegerField(default=0)
    thumbnail = models.FileField(null=True, blank=True)
    description = models.CharField(max_length=255, null=True)

class Bookmarks(models.Model):
    uuid = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    user = models.OneToOneField(User)
    payloads = models.ManyToManyField('FeedObject')

class Feed(models.Model):
    uuid = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    user = models.OneToOneField(User)
    payloads = models.ManyToManyField('FeedObject')

class FeedObject(models.Model):
    contents = (('post', 'post'),('video', 'video'),('qpost', 'qpost'), ('photo','photo'))#quick post
    uuid = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    cuuid = models.UUIDField(editable=False)
    type = models.CharField(max_length=5, choices=contents)



def createFeed(sender, **kwargs):
    if kwargs['created']:
        if kwargs['instance'].is_admin == False:
            Feed.objects.create(user=kwargs['instance'])
            Bookmarks.objects.create(user=kwargs['instance'])

post_save.connect(createFeed, sender=User)
