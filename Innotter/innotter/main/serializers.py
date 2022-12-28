import io
from rest_framework import serializers
from rest_framework.parsers import JSONParser
from rest_framework.renderers import JSONRenderer

from .models import Page, Post, Tag

class PageSerializer(serializers.ModelSerializer):
    owner = serializers.HiddenField(default=serializers.CurrentUserDefault())
    class Meta:
        model = Page
        fields = '__all__'

class PostSerializer(serializers.ModelSerializer):
    class Meta:
        model = Post
        fields = '__all__'

class TagSerializer(serializers.ModelSerializer):
    class Meta:
        model = Tag
        fields = '__all__'


