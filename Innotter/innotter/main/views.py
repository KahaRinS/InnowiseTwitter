from django.forms import model_to_dict
from django.shortcuts import render
from rest_framework.response import Response
from .models import Post, Page
from users.models import CustomUser
from django.views.generic import DetailView
from rest_framework import generics
from .serializers import PageSerializer
from rest_framework.views import APIView
# Create your views here.

class PageAPIView(APIView):
    def get(self, request):
        lst = Page.objects.all().values()
        return Response({'posts': list(lst)})
    def post(self, request):
        post_new = Page.objects.create(
            name=request.data['name'],
            uuid=request.data['uuid'],
            owner_id=request.data['owner_id'],
            description=request.data['description']
        )
        return Response({'post': model_to_dict(post_new)})

#class PageAPIView(generics.ListAPIView):
#    queryset = Page.objects.all()
#    serializer_class = PageSerializer

def render_main_page(request):
    post = Post.objects.all()
    user = CustomUser.objects.all()
    page = Page.objects.all()
    followers = Page.objects.get(name="SashasPage").followers.all()
    return render(request, 'main/index.html', {'post': post, 'user': user, 'page': page, 'fols': followers})

def index(request):
    return render(request, 'main/index.html')


#класс для отображения странички пользователя
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