from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework import generics, viewsets, status
from .serializers import *
from rest_framework.response import Response
from rest_framework import permissions
from users.models import CustomUser
# Create your views here.

class CreateUserAPIView(APIView):
    # Allow any user (authenticated or not) to access this url
    # permission_classes = ()

    def post(self, request):
        user = request.data
        serializer = UserSerializer(data=user)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response(serializer.data, status=status.HTTP_201_CREATED)

class UserViewSet(viewsets.ModelViewSet):
    queryset = CustomUser.objects.all()
    serializer_class = UserDetailSerializer

class UserRegisterViewSet(viewsets.ModelViewSet):
    queryset = CustomUser.objects.all()
    serializer_class = CustomRegisterSerializer