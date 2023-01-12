# likes/api/mixins.py

from rest_framework.decorators import action
from rest_framework.response import Response

from . import services


class LikedMixin:
    @action(methods=['GET'], detail=True)
    def like(self, request, pk=None):
        if request.user and request.user.is_authenticated:
            obj = self.get_object()
            services.add_like(obj, request.user)
            return Response()
        else:
            return Response({'error': 'Authentication failed'})

    @action(methods=['GET'], detail=True)
    def unlike(self, request, pk=None):
        if request.user and request.user.is_authenticated:
            obj = self.get_object()
            services.remove_like(obj, request.user)
            return Response()
        else:
            return Response({'error': 'Authentication failed'})

    # @action(methods=['GET'], detail=True)
    # def fans(self, request, pk=None):
    #     obj = self.get_object()
    #     serializer = FanSerializer(obj, many=True)
    #     return Response(serializer.data)

class FollowMixin:
    @action(methods=['GET'], detail=True)
    def follow(self, request, pk=None):
        if request.user and request.user.is_authenticated:
            obj = self.get_object()
            services.add_follow(obj, request.user)
            return Response()
        else:
            return Response({'error': 'Authentication failed'})

    @action(methods=['GET'], detail=True)
    def unfollow(self, request, pk=None):
        if request.user and request.user.is_authenticated:
            obj = self.get_object()
            services.delete_follow(obj, request.user)
            return Response()
        else:
            return Response({'error': 'Authentication failed'})