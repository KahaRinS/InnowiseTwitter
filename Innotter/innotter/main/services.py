from django.contrib.auth import get_user_model
from django.contrib.contenttypes.models import ContentType

from .models import Page

User = get_user_model()


def add_like(obj, user):
    obj.like.add(user)
    return obj


def remove_like(obj, user):
    obj.like.remove(user)
    return obj


def add_follow(obj, user):
    if obj.is_private == True:
        obj.follow_requests.add(user)
    else:
        obj.followers.add(user)
    return obj

def delete_follow(obj, user):
    if user in obj.follow_requests.all():
        obj.follow_requests.remove(user)
    if user in obj.followers.all():
        obj.followers.remove(user)
    return obj
