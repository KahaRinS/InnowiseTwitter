# likes/api/mixins.py
from rest_framework import status
from rest_framework.decorators import action
from rest_framework.response import Response
from rest_framework.permissions import *

from .services import Likes, Follow


class LikedMixin:
    @action(methods=['GET'], detail=True, permission_classes=[IsAuthenticated])
    def like(self, request, pk=None):
        obj = self.get_object()
        Likes.add_like(obj, request.user)
        return Response(status=status.HTTP_201_CREATED)

    @action(methods=['GET'], detail=True, permission_classes=[IsAuthenticated])
    def unlike(self, request, pk=None):
        obj = self.get_object()
        Likes.remove_like(obj, request.user)
        return Response(status=status.HTTP_201_CREATED)


class FollowMixin:
    @action(methods=['GET'], detail=True, permission_classes=[IsAuthenticated])
    def follow(self, request, pk=None):
        obj = self.get_object()
        Follow.add_follow(obj, request.user)
        return Response(status=status.HTTP_201_CREATED)

    @action(methods=['GET'], detail=True, permission_classes=[IsAuthenticated])
    def unfollow(self, request, pk=None):
        obj = self.get_object()
        Follow.delete_follow(obj, request.user)
        return Response(status=status.HTTP_201_CREATED)
