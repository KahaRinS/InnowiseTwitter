"""innotter URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.1/topics/http/urls/
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
from django.urls import path, include
from main.views import *
from users.views import *
from rest_framework import routers

RouterUser = routers.SimpleRouter()
RouterUser.register(r'user', UserViewSet)

RouterRegister = routers.SimpleRouter()
RouterRegister.register(r'reg', UserRegisterViewSet)

RouterPage = routers.SimpleRouter()
RouterPage.register(r'page', PageViewSet)

RouterPost = routers.SimpleRouter()
RouterPost.register(r'post', PostViewSet)

RouterTag = routers.SimpleRouter()
RouterTag.register(r'tag', TagViewSet)

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/v1/drf-auth/', include('rest_framework.urls')),
    path('api/v1/', include(RouterPage.urls)),
    path('api/v1/', include(RouterPost.urls)),
    path('api/v1/', include(RouterTag.urls)),
    path('api/v1/', include(RouterUser.urls)),
    path('accounts/', include('django.contrib.auth.urls')),
    # path('api/v1/users/', include('users.urls')),
    path('api/v1/', include(RouterRegister.urls)),
]

