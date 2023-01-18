# from rest_auth.registration.serializers import RegisterSerializer
# from rest_auth.registration.app_settings import RegisterSerializer
from rest_framework import serializers
from .models import CustomUser


class UserSerializer(serializers.ModelSerializer):
    class Meta(object):
        model = CustomUser
        fields = ('email', 'first_name', 'last_name')
        # extra_kwargs = {'password': {'write_only': True}}
        read_only_fields = ('email',)

class UserDetailSerializer(serializers.ModelSerializer):
    class Meta(object):
        model = CustomUser
        fields = '__all__'

class CustomRegisterSerializer(serializers.Serializer):
    email = serializers.EmailField(required=True)
    password = serializers.CharField(write_only=True,)
    first_name = serializers.CharField(required=True)
    last_name = serializers.CharField(required=True)
    username = serializers.CharField(required=True)
    def get_cleaned_data(self):
        super(CustomRegisterSerializer, self).get_cleaned_data()
        return {
            'password': self.validated_data.get('password', ''),
            'username': self.validated_data.get('username', ''),
            'email': self.validated_data.get('email', ''),
            'first_name': self.validated_data.get('first_name', ''),
            'last_name': self.validated_data.get('last_name', ''),
        }

    def create(self, validated_data):
        user = CustomUser.objects.create(
            email = validated_data['email'],
            first_name = validated_data['first_name'],
            last_name = validated_data['last_name'],
            username = validated_data['username'],
        )
        user.set_password(validated_data['password'])
        user.save()
        return user