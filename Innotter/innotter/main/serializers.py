import io

from main.models import Page, Post, Tag
from rest_framework import serializers


class PageGetSerializer(serializers.ModelSerializer):
    class Meta:
        model = Page
        fields = ('name', 'is_private', 'description', 'image', 'owner', 'followers')

class PagePostPutSerializer(serializers.ModelSerializer):
    owner = serializers.HiddenField(default=serializers.CurrentUserDefault())
    class Meta:
        model = Page
        fields = ('name', 'is_private', 'description', 'tags', 'image', 'owner')

class PageAdminSerializer(serializers.ModelSerializer):
    owner = serializers.HiddenField(default=serializers.CurrentUserDefault())
    class Meta:
        model = Page
        fields = '__all__'

class PostCreateSerializer(serializers.ModelSerializer):
    pages = Page.objects.all()
    class Meta:
        model = Post
        fields = ('content', 'reply_to')

    def create(self, validated_data):
        validated_data['page'] = Page.objects.all().get(owner = self.context['request'].user.id)
        return Post.objects.create(**validated_data)

class PostUpdateSerializer(serializers.ModelSerializer):
    pages = Page.objects.all()
    class Meta:
        model = Post
        fields = ('content', 'reply_to')

class PostGetSerializer(serializers.ModelSerializer):
    class Meta:
        model = Post
        fields = ('content', 'reply_to','likes')

class PostAdminSerializer(serializers.ModelSerializer):
    class Meta:
        model = Post
        fields = '__all__'

class TagSerializer(serializers.ModelSerializer):
    class Meta:
        model = Tag
        fields = '__all__'



class FollowSerializer(serializers.ModelSerializer):
    class Meta:
        model = Page
        fields = (
            'followers'
        )