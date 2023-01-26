from django.urls import path, include
from rest_framework import routers

from main.views import PageViewSet, PostViewSet, TagViewSet

Router = routers.SimpleRouter()
Router.register(r'page', PageViewSet)
Router.register(r'post', PostViewSet)
Router.register(r'tag', TagViewSet)

urlpatterns = [
    path('', include(Router.urls)),
]