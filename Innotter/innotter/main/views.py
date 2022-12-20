from django.forms import model_to_dict
from django.shortcuts import render
from rest_framework.response import Response
from .models import Post, Page, Tag
from users.models import CustomUser
from django.views.generic import DetailView
from rest_framework import generics, viewsets
from .serializers import *
from rest_framework.views import APIView


# Create your views here.

class PageViewSet(viewsets.ModelViewSet):
    queryset = Page.objects.all()
    serializer_class = PageSerializer

class TagViewSet(viewsets.ModelViewSet):
    queryset = Tag.objects.all()
    serializer_class = TagSerializer

class PostViewSet(viewsets.ModelViewSet):
    queryset = Post.objects.all()
    serializer_class = PostSerializer

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


# def render_main_page(request):
#     post = Post.objects.all()
#     user = CustomUser.objects.all()
#     page = Page.objects.all()
#     followers = Page.objects.get(name="SashasPage").followers.all()
#     return render(request, 'main/index.html', {'post': post, 'user': user, 'page': page, 'fols': followers})
#
# def index(request):
#     return render(request, 'main/index.html')
#
#
# #класс для отображения странички пользователя
# class PageDetailView(DetailView):
#     #Добавление дополнительных моделей в DetailView
#     def get_context_data(self, **kwargs):
#         data = super().get_context_data(**kwargs)
#         followers = Page.objects.get(name="SashasPage").followers.all()
#         data['page_title'] = followers
#         return data
#     model = Page
#     template_name = "main/pageview.html"
#     context_object_name = 'page'
