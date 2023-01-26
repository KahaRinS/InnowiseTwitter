from rest_framework.decorators import permission_classes, action
from rest_framework import generics, viewsets, status
from users.serializers import LoginSerializer, RefreshSerializer, UserUpdateSerializer, CustomRegisterSerializer, \
    UserDetailSerializer, UserSerializer
from rest_framework.response import Response
from users.models import CustomUser
from rest_framework.permissions import AllowAny


# Create your views here.


class UserViewSet(viewsets.ModelViewSet):
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
            response = Response(data=response_data)
            response.set_cookie(key='refreshtoken', value=response_data['refresh'], httponly=True)
            return response

        return Response(data=serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    @action(methods=['post'], detail=False, permission_classes=[AllowAny])
    def refresh(self, request):
        serializer = RefreshSerializer(data=request.data)
        if serializer.is_valid():
            response_data = serializer.save()
            response = Response(data=response_data)
            response.set_cookie(key='refreshtoken', value=response_data['refresh'], httponly=True)
            return response

        return Response(data=serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def get_serializer_class(self):
        if self.request.method == 'PUT':
            return UserUpdateSerializer
        if self.request.method == 'POST':
            return CustomRegisterSerializer
        if self.request.user.is_authenticated:
            if self.request.user.role == 'admin' or self.request.user.role == 'moderator':
                return UserDetailSerializer
            elif self.request.user.role == 'user':
                return UserSerializer
        else:
            return UserSerializer

