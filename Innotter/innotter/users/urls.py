from rest_framework import routers
from users.views import UserViewSet
from django.urls import path, include

Router = routers.SimpleRouter()
Router.register(r'page', UserViewSet)

urlpatterns = [
    path('', include(Router.urls)),
]