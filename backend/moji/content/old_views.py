from django.views.generic.edit import CreateView, UpdateView
from django.http import HttpResponse
#from content.models import Content, Comment, Like, CommentLike, Playlist
#from product.models import Points, PointsWallet
from django.urls import reverse
from .forms import CommentForm, LikeForm

class createPlaylist(CreateView):
    model = Playlist
    fields = ['name', 'description', 'thumbnail']
    template_name = 'pages/3/createpost.html'
    #success_url = reverse('home:home')

    def form_valid(self, form):
        form.instance.user = self.request.user
        form.instance.typeContent = 'Video'
        return super(videoCreate, self).form_valid(form)

def deletePlaylist(request, uuid):
    try:
        playlist = Playlist.objects.get(uuid=uuid)
    except Playlist.DoesNotExist:
        raise Http404('cant find this playlist')
    if request.user == playlist.user:
        playlist.delete()
        return redirect(reverse('home:home'))
    else:
        return redirect(reverse('home:home'))

def addContentToPlaylist(request, uuid, p_uuid):
    try:
        content = Content.objects.get(uuid=uuid)
        playlist = Playlist.objects.get(uuid=p_uuid)
    except Content.DoesNotExist:
        raise Http404('cant find this comment')
    playlist.add(content)
    return redirect(reverse('content:playlistdetail', kwargs={'uuid':playlist.uuid}))

def removeContentFromPlaylist(request, uuid, p_uuid):
    try:
        content = Content.objects.get(uuid=uuid)
        #playlist = content.playlist.get(uuid=p_uuid)
        playlist = Playlist.objects.get(uuid=p_uuid)
    except Content.DoesNotExist:
        raise Http404('cant find this comment')
    if request.user == playlist.user:
        playlist.remove(content)
        return redirect(reverse('content:playlistdetail', kwargs={'uuid':playlist.uuid}))
    else:
        return redirect(reverse('home:home'))

def detailPlaylist(request, uuid):
    playlist = Playlist.objects.get(uuid=uuid)
    return render(request,'pages/3/playlistdetail.html', {'playlist':playlist})

def createCommentLike(request, uuid):
    try:
        comment = Comment.objects.get(uuid=uuid)
        content_uuid = comment.ParentContent.uuid
        #content = Content.objects.get(uuid=newuuid)
    except Comment.DoesNotExist:
        raise Http404('cant find this comment')
    a = CommentLike.objects.create(user=request.user, ParentComment=comment)
    return redirect(reverse('content:detail', kwargs={'uuid':content_uuid}))

def removeCommentLike(request, uuid):
    try:
        commentLike = CommentLike.objects.get(uuid=uuid)
        content_uuid = commentLike.ParentComment.ParentContent.uuid
        #content = Content.objects.get(uuid=newuuid)
    except Content.DoesNotExist:
        raise Http404('cant find this content')
    if request.user == commentLike.user:
        commentLikelike.delete()
        return redirect(reverse('content:detail', kwargs={'uuid':content_uuid}))
    else:
        return redirect(reverse('home:home'))

def createLike(request, uuid):
    try:
        content = Content.objects.get(uuid=uuid)
    except Content.DoesNotExist:
        raise Http404('cant find this content')
    a = Like.objects.create(user=request.user, ParentContent=content)
    return redirect(reverse('content:detail', kwargs={'uuid':content.uuid}))

def removeLike(request, uuid):
    try:
        like = Like.objects.get(uuid=uuid)
        content_uuid = like.ParentContent.uuid
        #content = Content.objects.get(uuid=newuuid)
    except Content.DoesNotExist:
        raise Http404('cant find this content')
    if request.user == commentLike.user:
        like.delete()
        return redirect(reverse('content:detail', kwargs={'uuid':content_uuid}))
    else:
        return redirect(reverse('home:home'))

def detailContent(request, uuid):
    try:
        content = Content.objects.get(uuid=uuid)
    except Content.DoesNotExist:
        raise Http404('cant find this content')
    if content.user not in request.user.profile.following.all():
        return redirect(reverse('home:home'))
    content.views += 1
    content.save()
    return render(request, 'pages/3/contentdetail.html', {'content':content})

#need to get item and then delete
def deleteContent(request, uuid):
    content = Content.objects.get(uuid=uuid)
    if content.user == request.user:
        content.delete()
        return redirect(reverse('content:CreatePost'))
    else:
        #return them back to the content
        return redirect(reverse('account:ProfileView', kwargs={'name':content.user.username}))

def deleteComment(request, uuid):
    content = Comment.objects.get(uuid=uuid)
    content.delete()
    a = request.user.pointswallet_set.get(name=post.user.username)
    a.amount -= post.user.points.comment
    a.save()
    return redirect(reverse('home:home'))

def deleteLike(request, uuid):
    content = Like.objects.get(uuid=uuid)
    content.delete()
    #this is how points are deleted when unliking
    a = request.user.pointswallet_set.get(name=post.user.username)
    a.amount -= post.user.points.like
    a.save()
    return redirect(reverse('home:home'))

#need to handle unauthorized user, use middleware
class postCreate(CreateView):
    model = Content
    fields = ['file', 'caption']
    template_name = 'pages/3/createpost.html'
    #success_url = '/content/create/post'

    def form_valid(self, form):
        form.instance.user = self.request.user
        form.instance.typeContent = 'Post'
        return super(postCreate, self).form_valid(form)

class videoCreate(CreateView):
    model = Content
    fields = ['file', 'caption', 'thumbnail']
    template_name = 'pages/3/createpost.html'
    #success_url = reverse('home:home')

    def form_valid(self, form):
        form.instance.user = self.request.user
        form.instance.typeContent = 'Video'
        return super(videoCreate, self).form_valid(form)


class tweetCreate(CreateView):
    model = Content
    fields = ['caption',]
    template_name = 'pages/3/createpost.html'
    #success_url = reverse('home:home')

    def form_valid(self, form):
        form.instance.user = self.request.user
        form.instance.typeContent = 'Tweet'
        return super(tweetCreate, self).form_valid(form)

def commentCreate(request, uuid):
    try:
        post = Content.objects.get(uuid=uuid)
    except Content.DoesNotExist:
        raise Http404('this content does not exist, sorry')
    if request.method == "POST":
        form = CommentForm(request.POST)
        if form.is_valid():
            comment = form.save(commit=False)
            comment.ParentContent = post
            comment.user = request.user
            comment.comment = form.cleaned_data['comment']
            comment.save()
            if post.comment_set.filter(user=request.user).count() > post.user.points.comment_limit:
                return None
            else:
                a = request.user.pointswallet_set.get(name=post.user.username)
                a.amount += post.user.points.comment
                a.save()
                return redirect(reverse('content:detail', kwargs={'uuid':post.uuid}))
    else:
        form = CommentForm()
    return render(request, 'pages/4/createcomment.html', {'form': form})

def likeCreate(request, uuid):
    try:
        post = Content.objects.get(uuid=uuid)
    except Content.DoesNotExist:
        raise Http404('this content does not exist, sorry')
    if request.method == "POST":
        form = LikeForm(request.POST)
        if form.is_valid():
            comment = form.save(commit=False)
            comment.ParentContent = post
            comment.user = request.user
            comment.like = form.cleaned_data['like']
            comment.save()
            #this is how points are added
            if post.comment_set.filter(user=request.user).count() > post.user.points.like_limit:
                return None
            else:
                a = request.user.pointswallet_set.get(name=post.user.username)
                a.amount += post.user.points.like
                a.save()
                return redirect(reverse('content:detail', kwargs={'uuid':post.uuid}))
    else:
        form = LikeForm()
    return render(request, 'pages/4/createlike.html', {'form': form})
