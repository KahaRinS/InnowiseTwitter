from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='feeed'),
    path('mypage', views.mypage, name='mypage')
]
