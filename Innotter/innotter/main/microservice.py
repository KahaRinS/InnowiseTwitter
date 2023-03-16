from django.core.exceptions import ObjectDoesNotExist
import logging
from main.models import Like, Page, Post
from main.producer import publish


def update(owner):
    try:
        page_id = Page.objects.get(owner = owner).uuid
        likes = Like.objects.filter(post__page__owner=owner).count()
        posts = Post.objects.filter(page__owner = owner).count()
        subscribers = Page.objects.get(owner = owner).followers.all().count()
    except ObjectDoesNotExist:
        logging.error('Page does not exist')
    publish('quote_created', {'page_id': page_id, 'subscribers': subscribers, 'posts': posts, 'likes': likes}, 'like')