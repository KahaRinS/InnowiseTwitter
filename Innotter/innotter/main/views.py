from django.contrib.auth import get_user_model
from rest_framework.decorators import action

from main.mixins import FollowMixin, LikedMixin, UuidMixin
from main.models import Page, Post, Tag
from main.permissions import (IsOwnerOrAdminOrReadOnly,
                              IsPostOwnerOrAdminOrReadOnly)
from main.serializers import (PageAdminSerializer, PageGetSerializer,
                              PagePostPutSerializer, PostAdminSerializer,
                              PostCreateSerializer, PostGetSerializer,
                              PostUpdateSerializer, TagSerializer)
from main.filters import PageFilter
from django_filters.rest_framework import DjangoFilterBackend
from rest_framework import generics, status, viewsets
from rest_framework.permissions import IsAuthenticatedOrReadOnly
from rest_framework.response import Response


class NewsViewSet(viewsets.ModelViewSet):
    queryset = Post.objects.all()
    serializer_class = PostGetSerializer
    def list(self, request, *args, **kwargs):
        AllPosts = self.filter_queryset(self.get_queryset())
        AllPages = Page.objects.all()
        UserFollows = AllPages.filter(followers=request.user)
        Posts = []
        for post in AllPosts:
            for page in UserFollows:
                if post.page == page:
                   Posts.append(post)
        print(Posts)
        serializer = self.get_serializer(Posts, many=True)
        return Response(serializer.data)
    def create(self, request):
        return Response(status=status.HTTP_405_METHOD_NOT_ALLOWED)
    def retrieve(self, request, *args, **kwargs):
        return Response(status=status.HTTP_405_METHOD_NOT_ALLOWED)
    def update(self, request, *args, **kwargs):
        return Response(status=status.HTTP_405_METHOD_NOT_ALLOWED)
    def destroy(self, request, *args, **kwargs):
        return Response(status=status.HTTP_405_METHOD_NOT_ALLOWED)

class PageViewSet(FollowMixin, viewsets.ModelViewSet):
    queryset = Page.objects.all()
    serializer_class = PageGetSerializer
    filter_backends = (DjangoFilterBackend, )
    permission_classes = (IsAuthenticatedOrReadOnly, IsOwnerOrAdminOrReadOnly)
    filterset_class = PageFilter


    def create(self, request, *args, **kwargs):
        user_has_page = Page.objects.filter(owner=request.user).exists()
        if user_has_page:
            return Response({'error': 'User already have a page'}, status= status.HTTP_409_CONFLICT)
        else:
            serializer = self.get_serializer(data=request.data)
            serializer.is_valid(raise_exception=True)
            self.perform_create(serializer)
            headers = self.get_success_headers(serializer.data)
            return Response(serializer.data, status=status.HTTP_201_CREATED, headers=headers)

    def retrieve(self, request, *args, **kwargs):
        instance = self.get_object()
        serializer = self.get_serializer(instance)
        if instance.is_private and not(request.user.is_staff) and not(instance.owner == request.user):
            return Response({'error': 'Page is private', 'name': instance.name})
        return Response(serializer.data)

    def list(self, request, *args, **kwargs):
        queryset = self.filter_queryset(self.get_queryset())
        if not request.user.is_staff:
            queryset = queryset.filter(is_private=False)
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
            instance._prefetched_objects_cache = {}

        return Response(serializer.data)

    @action(detail=True, methods=['get'])
    def uuid(self, request, pk=None):
        uuid = pk
        instance = self.get_queryset().get(uuid=uuid)
        serializer = self.get_serializer(instance)
        if instance.is_private and not (request.user.is_staff) and not (instance.owner == request.user):
            return Response({'error': 'Page is private', 'name': instance.name})
        return Response(serializer.data)

    def get_serializer_class(self):
        User = get_user_model()
        if self.request.user.is_authenticated:
            if self.request.user.role == User.Roles.USER:
                if self.action == 'retrieve' or self.action == 'list':
                    return PageGetSerializer
                elif self.action == 'create' or self.action == 'update':
                    return PagePostPutSerializer
            if self.request.user.role == User.Roles.ADMIN or self.request.user.is_staff:
                return PageAdminSerializer
        else:
            return PageGetSerializer


class TagViewSet(viewsets.ModelViewSet):
    queryset = Tag.objects.all()
    serializer_class = TagSerializer

class PostViewSet(LikedMixin, viewsets.ModelViewSet):
    queryset = Post.objects.all()
    permission_classes = (IsAuthenticatedOrReadOnly,IsPostOwnerOrAdminOrReadOnly)
    def create(self, request, *args, **kwargs):
        user_has_page = Page.objects.filter(owner=request.user).exists()
        context = {'request': request}
        if user_has_page:
            serializer = self.get_serializer(data=request.data, context=context)
            serializer.is_valid(raise_exception=True)
            self.perform_create(serializer)
            headers = self.get_success_headers(serializer.data)
            return Response(serializer.data, status=status.HTTP_201_CREATED, headers=headers)
        else:
            return Response({'error': 'User has not page'})

    def get_serializer_class(self):
        User = get_user_model()
        if self.request.user.is_authenticated:
            if self.request.user.role == User.Roles.USER:
                if self.action == 'retrieve' or self.action == 'list':
                    return PostGetSerializer
                elif self.action == 'create':
                    return PostCreateSerializer
                elif self.action == 'update':
                    return PostUpdateSerializer
            if self.request.user.role == User.Roles.ADMIN or self.request.user.is_staff:
                if self.action == 'retrieve' or self.action == 'list':
                    return PostAdminSerializer
                elif self.action == 'create':
                    return PostCreateSerializer
                elif self.action == 'update':
                    return PostAdminSerializer
        else:
            return PostGetSerializer