from django.shortcuts import render
from django.http import HttpResponse


def index(request):
    dict = {
        'title':'Заголовок главной страницы',
        'body':'Тело главной страницы'
    }
    return render(request, 'main/index.html', dict)

def mypage(request):
    return render(request, 'main/page.html')