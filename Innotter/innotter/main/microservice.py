import logging

from django.core.exceptions import ObjectDoesNotExist
from main.models import Like, Page, Post
from main.producer import publish


def update_page_statistics(owner):
    try:
        page = Page.objects.get(owner=owner)
        posts_count = page.posts.count()
        likes_count = Like.objects.filter(post__page__owner=owner).count()
        subscribers_count = page.followers.count()
        publish('quote_created',
                {'page_id': page.uuid, 'subscribers': subscribers_count, 'posts': posts_count, 'likes': likes_count},
                'like')
    except ObjectDoesNotExist:
        logging.error('Page does not exist')
