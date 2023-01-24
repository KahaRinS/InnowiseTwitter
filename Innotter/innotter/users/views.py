from django.shortcuts import render
from django.views.decorators.csrf import ensure_csrf_cookie
from rest_framework.decorators import permission_classes
from rest_framework.permissions import AllowAny
from rest_framework.views import APIView
from rest_framework import generics, viewsets, status
from .serializers import *
from rest_framework.response import Response
from rest_framework import permissions
from users.models import CustomUser
import json
from rest_framework.permissions import *
from django.http import HttpResponse


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
    def get_serializer_class(self):
        if self.request.method == 'PUT':
            return UserUpdateSerializer
        if self.request.method == 'POST':
            return CustomRegisterSerializer
        if self.request.user.is_authenticated:
            if self.request.user.role == 'admin' or self.request.user.role == 'moderator':
                return UserDetailSerializer
            else:
                if self.request.user.role == 'user':
                    return UserSerializer
        else:
            return UserSerializer

class UserRegisterViewSet(viewsets.ModelViewSet):
    queryset = CustomUser.objects.all()
    serializer_class = CustomRegisterSerializer

class LoginView(APIView):
    permission_classes = (AllowAny,)

    def post(self, request, format=None):
        serializer = LoginSerializer(data=request.data)
        if serializer.is_valid():
            response_data = serializer.save()
            response = Response(data=response_data)
            response.set_cookie(key='refreshtoken', value=response_data['refresh'], httponly=True)
            return response

        return Response(data=serializer.errors, status=status.HTTP_400_BAD_REQUEST)

class RefreshView(APIView):

    def post(self, request, format=None):
        serializer = RefreshSerializer(data=request.data)
        if serializer.is_valid():
            response_data = serializer.save()
            response = Response(data=response_data)
            response.set_cookie(key='refreshtoken', value=response_data['refresh'], httponly=True)
            return response

        return Response(data=serializer.errors, status=status.HTTP_400_BAD_REQUEST)