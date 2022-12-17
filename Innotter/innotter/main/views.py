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
        p = Page.objects.all()
        return Response({'pages': PageSerializer(p, many=True).data})
    # def get(self, request, *args, **kwargs):
    #     pk = kwargs.get("pk", None)
    #     p = Page.objects.get(pk=pk)
    #     return Response({'pages': PageSerializer(p).data})
    def post(self, request):
        serializer = PageSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response({'page': serializer.data})

    def put(self, request, *args, **kwargs):
        pk = kwargs.get("pk", None)
        if not pk:
            return Response({"error":"Method PUT not allowed"})

        try:
            instance = Page.objects.get(pk=pk)
        except:
            return Response({"error": "Object does not exists"})

        serializer = PageSerializer(data=request.data, instance=instance)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response({"page": serializer.data})
    def delete(self, request, *args, **kwargs):
        pk = kwargs.get("pk", None)
        if not pk:
            return Response({"error":"Methode DELETE not allowed"})
        try:
            instance = Page.objects.get(pk=pk)
        except:
            return Response({"error": "Object does not exists"})
        instance.delete()
        return Response({"page":"delete page" + str(pk)})

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