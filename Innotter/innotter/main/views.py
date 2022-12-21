from django.forms import model_to_dict
from django.shortcuts import render
from rest_framework.decorators import action
from rest_framework.permissions import IsAuthenticatedOrReadOnly
from rest_framework.response import Response
from .models import Post, Page, Tag
from users.models import CustomUser
from django.views.generic import DetailView
from rest_framework import generics, viewsets
from .serializers import *
from .permissions import IsOwnerOrAdminOrReadOnly
from rest_framework.views import APIView


# Create your views here.


class PageViewSet(viewsets.ModelViewSet):
    queryset = Page.objects.all()
    serializer_class = PageSerializer
    permission_classes = (IsAuthenticatedOrReadOnly, IsOwnerOrAdminOrReadOnly)

    def retrieve(self, request, *args, **kwargs):
        instance = self.get_object()
        serializer = self.get_serializer(instance)
        print(instance.followers.all())
        print(request.user)
        pages = PageViewSet.queryset
        for page in instance.followers.all():
            print(page, end="\n\n")
        if instance.is_private and not(request.user.is_staff) and not(instance.owner == request.user):
            return Response({'error': 'Page is private', 'name': instance.name})
        return Response(serializer.data)

    def list(self, request, *args, **kwargs):

        queryset = self.filter_queryset(self.get_queryset())
        print(queryset)
        page = self.paginate_queryset(queryset)
        if page is not None:
            serializer = self.get_serializer(page, many=True)
            return self.get_paginated_response(serializer.data)

        serializer = self.get_serializer(queryset, many=True)
        return Response(serializer.data)


class TagViewSet(viewsets.ModelViewSet):
    queryset = Tag.objects.all()
    serializer_class = TagSerializer

class PostViewSet(viewsets.ModelViewSet):
    queryset = Post.objects.all()
    serializer_class = PostSerializer
    permission_classes = (IsAuthenticatedOrReadOnly, IsOwnerOrAdminOrReadOnly)

# class PageAPIList(generics.ListCreateAPIView):
#     queryset = Page.objects.all()
#     serializer_class = PageSerializer
#
# class PageAPIUpdate(generics.UpdateAPIView):
#     queryset = Page.objects.all()
#     serializer_class = PageSerializer
#
# class PageAPIDetailView(generics.RetrieveUpdateDestroyAPIView):
#     queryset = Page.objects.all()
#     serializer_class = PageSerializer


def render_main_page(request):
    post = Post.objects.all()
    user = CustomUser.objects.all()
    page = Page.objects.all()
    followers = Page.objects.get(name="SashasPage").followers.all()
    return render(request, 'main/index.html', {'post': post, 'user': user, 'page': page, 'fols': followers})
#
# def index(request):
#     return render(request, 'main/index.html')
#
#
# #класс для отображения странички пользователя
class PageDetailView(DetailView):
    #Добавление дополнительных моделей в DetailView
    def get_context_data(self, **kwargs):
        data = super().get_context_data(**kwargs)
        followers = Page.objects.get(name="SashasPage").followers.all()
        data['page_title'] = followers
        return data
    model = Page
    template_name = "main/pageview.html"
    context_object_name = 'page'
