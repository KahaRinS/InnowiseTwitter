from django.shortcuts import render
from .models import Post
from users.models import CustomUser
# Create your views here.

def render_main_page(request):
    post = Post.objects.all()
    user = CustomUser.objects.all()
    return render(request, 'main/index.html', {'post': post, 'user': user})

def index(request):
    return render(request, 'main/index.html')