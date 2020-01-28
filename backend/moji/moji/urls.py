"""moji URL Configuration!

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.11/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.conf.urls import url, include
    2. Add a URL to urlpatterns:  url(r'^blog/', include('blog.urls'))
"""
from django.conf.urls import url, include
from django.contrib import admin
from django.conf.urls.static import static
from django.conf import settings
from django.contrib.auth.views import login, logout
from . import views
urlpatterns = [
    url(r'^admin/', admin.site.urls),
    url(r'^account/', include('account.urls')),
    url(r'^$', views.home),
    url(r'^feed/home/$', views.feed, name='feed'),
    url(r'^content/', include('content.urls')),
    #url(r'^home/', include('home.urls')),
    #url(r'^product/', include('product.urls')),
    #url(r'^banking/', include('banking.urls')),
    #url(r'^notification/', include('notif.urls')),
    url(r'', include('django.contrib.auth.urls'))
]

#urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
