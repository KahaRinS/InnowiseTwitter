import io
from rest_framework import serializers


from .models import Page, Post, Tag

class PageSerializer(serializers.ModelSerializer):
    owner = serializers.HiddenField(default=serializers.CurrentUserDefault())
    class Meta:
        model = Page
        fields = ('name', 'is_private', 'uuid', 'description', 'tags', 'image', 'owner', 'followers')

class PageAdminSerializer(serializers.ModelSerializer):
    class Meta:
        model = Page
        fields = '__all__'

class PostSerializer(serializers.ModelSerializer):
    pages = Page.objects.all()
    class Meta:
        model = Post
        fields = ('content', 'reply_to','like',)

    def create(self, validated_data):
        pages = Page.objects.all()
        print(self.context['request'].user.id)
        validated_data['page'] = pages.get(owner = self.context['request'].user.id)

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