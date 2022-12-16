from django.urls import path
from . import views

urlpatterns = [
    path('', views.render_main_page, name="home"),
    path('page/<int:pk>', views.PageDetailView.as_view(), name='page')
]