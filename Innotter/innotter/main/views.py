from rest_framework.permissions import IsAuthenticatedOrReadOnly
from rest_framework.response import Response
from .models import Post, Page, Tag
from users.models import CustomUser
from rest_framework import generics, viewsets, status
from .serializers import *
from .permissions import IsOwnerOrAdminOrReadOnly, IsPostOwnerOrAdminOrReadOnly
from .mixins import LikedMixin, FollowMixin



# Create your views here.


class PageViewSet(FollowMixin,viewsets.ModelViewSet):
    queryset = Page.objects.all()
    serializer_class = PageSerializer
    permission_classes = (IsAuthenticatedOrReadOnly, IsOwnerOrAdminOrReadOnly)


    def retrieve(self, request, *args, **kwargs):
        print(request.content_type)
        instance = self.get_object()
        serializer = self.get_serializer(instance)
        if instance.is_private and not(request.user.is_staff) and not(instance.owner == request.user):
            return Response({'error': 'Page is private', 'name': instance.name})
        return Response(serializer.data)

    def list(self, request, *args, **kwargs):
        print(request.user.role)
        queryset = self.filter_queryset(self.get_queryset())
        if not request.user.is_staff:
            queryset = queryset.filter(is_private=True)
        page = self.paginate_queryset(queryset)
        if page is not None:
            serializer = self.get_serializer(page, many=True)
            return self.get_paginated_response(serializer.data)

        serializer = self.get_serializer(queryset, many=True)
        return Response(serializer.data)

    def update(self, request, *args, **kwargs):
        partial = kwargs.pop('partial', False)
        instance = self.get_object()
        serializer = self.get_serializer(instance, data=request.data, partial=partial)
        serializer.is_valid(raise_exception=True)
        self.perform_update(serializer)

        if getattr(instance, '_prefetched_objects_cache', None):
            # If 'prefetch_related' has been applied to a queryset, we need to
            # forcibly invalidate the prefetch cache on the instance.
            instance._prefetched_objects_cache = {}

        return Response(serializer.data)


    def get_serializer_class(self):
        if self.request.user.is_authenticated:
            if self.request.user.role == 'user':
                return PageSerializer
            else:
                return PageAdminSerializer
        else:
            return PageSerializer


class TagViewSet(viewsets.ModelViewSet):
    queryset = Tag.objects.all()
    serializer_class = TagSerializer
    permission_classes = (IsAuthenticatedOrReadOnly)

class PostViewSet(LikedMixin, viewsets.ModelViewSet):
    queryset = Post.objects.all()
    serializer_class = PostSerializer
    permission_classes = (IsAuthenticatedOrReadOnly,IsPostOwnerOrAdminOrReadOnly)
    def create(self, request, *args, **kwargs):
        pages = Page.objects.all()
        user_has_page = 0
        context = {'request': request}
        for page in pages:
            if page.owner == request.user:
                user_has_page = 1
        if user_has_page:
            serializer = PostSerializer(data=request.data, context=context)
            serializer.is_valid(raise_exception=True)
            self.perform_create(serializer)
            headers = self.get_success_headers(serializer.data)
            return Response(serializer.data, status=status.HTTP_201_CREATED, headers=headers)
        else:
            return Response({'error': 'User has not page'})

    def get_serializer_class(self):
        if self.request.user.is_authenticated:
            if self.request.user.role == 'user':
                return PostSerializer
            else:
                return PostAdminSerializer
        else:
            return PostSerializer