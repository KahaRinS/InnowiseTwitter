import io
from rest_framework import serializers
from rest_framework.parsers import JSONParser
from rest_framework.renderers import JSONRenderer

from .models import Page, Post, Tag


# class PageModel:
#     def __init__(self, name, description, owner_id):
#         self.name = name
#         self.description = description
#         self.owner_id = owner_id

class PageSerializer(serializers.ModelSerializer):
    class Meta:
        model = Page
        fields = "__all__"

class PostSerializer(serializers.ModelSerializer):
    class Meta:
        model = Post
        fields = "__all__"

class TagSerializer(serializers.ModelSerializer):
    class Meta:
        model = Tag
        fields = "__all__"


# def encode():
#     model = PageModel('second Love Page', 'Description: Love Page second bla vla', 8)
#     model_sr = PageSerializer(model)
#     print(model_sr.data, type(model_sr.data), sep='\n')
#     json = JSONRenderer().render(model_sr.data)
#     print(json)
#
# def decode():
#     stream = io.BytesIO(b'{"name":"second Love Page","description":"Description: Love Page second bla vla","owner_id":8}')
#     data = JSONParser().parse(stream)
#     serializers = PageSerializer(data=data)
#     serializers.is_valid()
#     print(serializers.validated_data)