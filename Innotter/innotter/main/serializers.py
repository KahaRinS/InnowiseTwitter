import io

from main.models import Page, Post, Tag
from rest_framework import serializers


class PageSerializer(serializers.ModelSerializer):
    owner = serializers.HiddenField(default=serializers.CurrentUserDefault())
    class Meta:
        model = Page
        fields = ('id','name', 'is_private', 'uuid', 'description', 'tags', 'image','owner', 'followers')

class PageAdminSerializer(serializers.ModelSerializer):
    owner = serializers.HiddenField(default=serializers.CurrentUserDefault())
    class Meta:
        model = Page
        fields = '__all__'

class PostSerializer(serializers.ModelSerializer):
    pages = Page.objects.all()
    class Meta:
        model = Post
        fields = ('id','content', 'reply_to','likes')

    def create(self, validated_data):
        validated_data['page'] = Page.objects.all().get(owner = self.context['request'].user.id)
        return Post.objects.create(**validated_data)

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