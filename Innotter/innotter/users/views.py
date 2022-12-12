from django.shortcuts import render

from users.forms import CustomUserCreationForm
from users.models import CustomUser
from django.urls import reverse_lazy
from django.contrib.auth.forms import UserCreationForm
from django.views.generic.edit import CreateView
# Create your views here.

def render_signup_page(request):
    user = CustomUser.objects.all()
    return render(request, 'users/signup.html', {'user': user})

def login(request):
    return render(request, 'users/login.html')

class SignUp(CreateView):
    form_class = CustomUserCreationForm
    success_url = reverse_lazy("login")
    template_name = "users/signup.html"