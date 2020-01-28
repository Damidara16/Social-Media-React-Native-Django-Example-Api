from django.conf.urls import url
from django.contrib.auth.views import login, logout
from . import views

app_name = 'content'

urlpatterns = [
    url(r'^detail/(?P<uuid>[\w]{8}(-[\w]{4}){3}-[\w]{12})/$', views.get_content_detail, name='detail'),
    ]
"""#delete content
    url(r'^delete/content/(?P<uuid>[\w]{8}(-[\w]{4}){3}-[\w]{12})/$', views.delete_content, name='DeleteContent'),
#delete comment
    url(r'^delete/comment/(?P<uuid>[\w]{8}(-[\w]{4}){3}-[\w]{12})/$', views.delete_comment, name='DeleteComment'),
#delete like
    url(r'^delete/like/(?P<uuid>[\w]{8}(-[\w]{4}){3}-[\w]{12})/$', views.deleteLike, name='DeleteLike'),
#comment create
    url(r'^create/comment/(?P<uuid>[\w]{8}(-[\w]{4}){3}-[\w]{12})/$', views.create_comment, name='CreateComment'),
#comment create
    url(r'^get/comments/(?P<uuid>[\w]{8}(-[\w]{4}){3}-[\w]{12})/$', views.get_content_comments, name='CreateLike'),

    url(r'^create/cs/(?P<uuid>[\w]{8}(-[\w]{4}){3}-[\w]{12})/$', views.send_content_share, name='unLike'),

    url(r'^manage/cs/(?P<uuid>[\w]{8}(-[\w]{4}){3}-[\w]{12})/$', views.manage_content_share, name='createLike'),

    url(r'^CMunlike/(?P<uuid>[\w]{8}(-[\w]{4}){3}-[\w]{12})/$', views.removeCommentLike, name='Comment_unLike'),

    url(r'^CMlike/(?P<uuid>[\w]{8}(-[\w]{4}){3}-[\w]{12})/$', views.createCommentLike, name='Comment_createLike'),

    url(r'^like/(?P<uuid>[\w]{8}(-[\w]{4}){3}-[\w]{12})/$', views.detailPlaylist, name='detailPlaylist'),

    url(r'^addPlaylist/(?P<uuid>[\w]{8}(-[\w]{4}){3}-[\w]{12})/(?P<p_uuid>[\w]{8}(-[\w]{4}){3}-[\w]{12})/$', views.addContentToPlaylist, name='addContentPlaylist'),

    url(r'^removePlaylist/(?P<uuid>[\w]{8}(-[\w]{4}){3}-[\w]{12})/(?P<p_uuid>[\w]{8}(-[\w]{4}){3}-[\w]{12})/$', views.removeContentFromPlaylist, name='removeContentPlaylist'),

    url(r'^delete_playlist/(?P<uuid>[\w]{8}(-[\w]{4}){3}-[\w]{12})/$', views.deletePlaylist, name='deletePlaylist'),

    url(r'^creating_playlist/$', views.createPlaylist, name='createPlaylist'),
"""
