# likes/api/mixins.py

from rest_framework.decorators import action
from rest_framework.response import Response

from . import services
from .serializers import FanSerializer
from .serializers import PostSerializer


class LikedMixin:
    @action(methods=['POST'], detail=True)
    def like(self, request, pk=None):
        obj = self.get_object()
        services.add_like(obj, request.user)
        return Response()

    @action(methods=['POST'], detail=True)
    def unlike(self, request, pk=None):
        obj = self.get_object()
        services.remove_like(obj, request.user)
        return Response()

    @action(methods=['GET'], detail=True)
    def fans(self, request, pk=None):
        obj = self.get_object()
        fans = services.get_fans(obj)
        serializer = FanSerializer(fans, many=True)
        return Response(serializer.data)

class FollowMixin:
    @action(methods=['PUT'], detail=True)
    def follow(self, request, pk=None):
        obj = self.get_object()
        print(obj)
        services.add_follow(obj, request.user)
        return Response()

    @action(methods=['PUT'], detail=True)
    def unfollow(self, request, pk=None):
        obj = self.get_object()
        services.delete_follow(obj, request.user)
        return Response()
