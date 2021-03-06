"""octafit URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path,include
from welcome import views
from django.conf import settings

from django.views.static import serve



urlpatterns = [
    path('admin/', admin.site.urls),
    #toobar pattern
    path('__debug__/', include('debug_toolbar.urls')),
    #include will route to our app(welcome)
    path('welcome/',include('welcome.urls')),
    #name  is given for url redirect.(if needed)
    path('welcomes', views.welcomes,name="welcomes"),
    path('home', views.home,name="home"),
    path('register', views.register,name="register"),
    path('clientcount',views.clientcount),
    path('view',views.view,name="view"),
    path('view2',views.view2,name="view"),
    path('',views.welcomes,name="welcomes"),
    path('login',views.login,name="login"),
    path('signup',views.signup,name="signup"),
    path('edit1',views.edit1,name="edit1"),
    path('signout',views.signout,name="signout"),
    path(r'^media/(?P<path>.*)$', serve,{'document_root':       settings.MEDIA_ROOT}), 
    path(r'^static/(?P<path>.*)$', serve,{'document_root': settings.STATIC_ROOT}), 
    path('privacypolicy',views.privacypolicy,name="privacypolicy"),
]
 