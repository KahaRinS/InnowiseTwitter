import io

from rest_framework import serializers
from rest_framework.parsers import JSONParser
from rest_framework.renderers import JSONRenderer

from .models import Page


# class PageModel:
#     def __init__(self, name, description, owner_id):
#         self.name = name
#         self.description = description
#         self.owner_id = owner_id

class PageSerializer(serializers.ModelSerializer):
    name = serializers.CharField(max_length=80)
    description = serializers.CharField()
    owner_id = serializers.IntegerField()
    uuid = serializers.CharField(max_length=30)
    is_private = serializers.BooleanField(default=False)

    def create(self, validated_data):
        return Page.objects.create(**validated_data)

    def update(self, instance, validated_data):
        instance.name = validated_data.get("name", instance.name)
        instance.description = validated_data.get("description", instance.description)
        instance.owner_id = validated_data.get("owner_id", instance.owner_id)
        instance.uuid = validated_data.get("uuid", instance.uuid)
        instance.is_private = validated_data.get("is_private", instance.is_private)
        instance.save()
        return instance

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