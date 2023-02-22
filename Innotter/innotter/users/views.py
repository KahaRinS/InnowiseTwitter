from django.contrib.auth import get_user_model
from django_filters.rest_framework import DjangoFilterBackend
from rest_framework import generics, status, viewsets
from rest_framework.decorators import action, permission_classes
from rest_framework.permissions import AllowAny
from rest_framework.response import Response
from users.filters import UserFilter
from users.models import CustomUser
from users.serializers import (CustomRegisterSerializer, LoginSerializer,
                               RefreshSerializer, UserDetailSerializer,
                               UserSerializer, UserUpdateSerializer)

# Create your views here.


class UserViewSet(viewsets.ModelViewSet):
    filter_backends = (DjangoFilterBackend,)
    filterset_class = UserFilter
    queryset = CustomUser.objects.all()

    @action(methods=['post'], detail=False, permission_classes=[AllowAny])
    def register(self, request):
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        self.perform_create(serializer)
        headers = self.get_success_headers(serializer.data)
        return Response(serializer.data, status=status.HTTP_201_CREATED, headers=headers)

    @action(methods=['post'], detail=False, permission_classes=[AllowAny])
    def login(self, request):
        serializer = LoginSerializer(data=request.data)
        if serializer.is_valid():
            response_data = serializer.save()
            response = Response(data=response_data, status=status.HTTP_200_OK)
            response.set_cookie(key='refresh', value=response_data['refresh'], httponly=True)
            return response

        return Response(data=serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    @action(methods=['post'], detail=False, permission_classes=[AllowAny])
    def refresh(self, request):
        serializer = RefreshSerializer(data=request.data)
        if serializer.is_valid():
            response_data = serializer.save()
            response = Response(data=response_data, status=status.HTTP_200_OK)
            response.set_cookie(key='refresh', value=response_data['refresh'], httponly=True)
            return response

        return Response(data=serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def get_serializer_class(self):
        User = get_user_model()
        if self.action == 'update':
            return UserUpdateSerializer
        if self.action == 'create':
            return CustomRegisterSerializer
        if self.request.user.is_authenticated:
            if self.request.user.role == User.Roles.ADMIN or self.request.user.role == User.Roles.MODERATOR:
                return UserDetailSerializer
            elif self.request.user.role == User.Roles.USER:
                return UserSerializer
        else:
            return UserSerializer

