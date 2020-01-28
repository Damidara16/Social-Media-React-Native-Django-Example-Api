from django.conf.urls import url
#from django.contrib.auth.views import login, logout, PasswordResetView, PasswordResetDoneView, PasswordResetConfirmView, PasswordResetCompleteView
from . import views
from django.contrib.auth import views as auth_views

app_name = 'account'
urlpatterns = [
    url(r'^post/file/$',views.postFile,name='filepost'),
    url(r'^unauth/$',views.unauthed,name='unauthed'),
    url(r'^auth/$',views.authUser),
    url(r'^lastseen/$',views.send_lastSeen),
    url(r'^update/profile/$',views.update_user_or_profile),
    url(r'^create/user/$',views.create_user_and_profile),
    url(r'^manage/block_unblock/$',views.block_or_unblock_user),
    url(r'^delete/user/$', views.delete_user_and_profile),
    url(r'^get/user/(?P<username>\w+)/$',views.get_user_and_profile_with_content),
    url(r'^update/authed_password/$',views.change_user_password),
    #url(r'^get/follow_request/$', views.get_all_follow_requests),
    #url(r'^post/follow_request/$',views.send_follow_request),
    #url(r'^get/requests/$', views.manage_follow_request),
    #url(r'^delete/follow_request/$',views.unsend_follow_request),
    url(r'^get/following/$',views.get_following),
    url(r'^get/followers/$',views.get_followers),
    url(r'^post/remove_follower/$', views.remove_follower)
]
"""
urlpatterns = [
    url(r'^profile/(?P<name>\w+)/$', views.ViewProfile, name='ProfileView'),
    url(r'^login/$', login, {'template_name': 'pages/2/login.html'}, name='login'),
    url(r'^logout/$', logout, {'template_name': 'pages/2/loggedout.html'}, name='logout'),
    url(r'^following/(?P<name>\w+)/unfollowed/$', views.unfollowUser, name='Unfollow'),
    url(r'^following/requests/(?P<name>\w+)/$', views.detailRequests, name='detailAcceptance'),
    url(r'^following/requests/(?P<name>\w+)/accept/$', views.editRequests, name='editAcceptance'),
    url(r'^following/requests/(?P<name>\w+)/decline/$', views.deleteRequests, name='deleteAcceptance'),
    url(r'^following/requests/(?P<name>\w+)/sent/$', views.makeRequests, name='makeAcceptance'),
    url(r'^following/requests/$', views.listRequests, name='listAcceptance'),
    url(r'^register/$', views.register, name='Register'),
    url(r'^delete/$', views.deleteProfile, name='DeleteProfile'),
    url(r'^profile-edit/$', views.updateProfile, name='update'),
    url(r'^change-password/$', views.change_password, name='change_password'),
    url(r'^reset-password/$', PasswordResetView.as_view(), name='password_reset'),
    url(r'^reset-password/done/$', PasswordResetDoneView.as_view(), name='password_reset_done'),
    url(r'^reset-password/confirm/(?P<uidb64>[0-9A-Za-z]+)-(?P<token>.+)/$', PasswordResetConfirmView.as_view(), name='password_reset_confirm'),
    url(r'^reset-password/complete/$', PasswordResetCompleteView.as_view(), name='password_reset_complete'),
    url(r'^blocked/(?P<uuid>[\w]{8}(-[\w]{4}){3}-[\w]{12})/$', views.blockUser, name='blockUser'),
    url(r'unblocked/(?P<uuid>[\w]{8}(-[\w]{4}){3}-[\w]{12})/$', views.unblockUser, name='unblockUser'),
    url(r'preview/process/(?P<uuid>[\w]{8}(-[\w]{4}){3}-[\w]{12})/$', views.previewRemoveAdd, name='PreviewProcess'),
    #url(r'preview/remove/(?P<uuid>[\w]{8}(-[\w]{4}){3}-[\w]{12})/$', views.PreviewRemove, name='removePreview'),


#password reset  {'post_reset_redirect': 'account:password_reset_complete'}  {'post_reset_redirect': 'account:password_reset_done'},
]
"""
