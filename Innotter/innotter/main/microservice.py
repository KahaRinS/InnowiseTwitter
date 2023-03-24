from django.core.exceptions import ObjectDoesNotExist
import logging
from main.models import Like, Page, Post
from main.producer import publish


def update(owner):
    try:
        page = Page.objects.get(owner=owner)
        posts_count = page.posts.count()
        likes_count = Like.objects.filter(post__page__owner=owner).count()
        subscribers_count = page.followers.count()
        publish('quote_created',
                {'page_id': str(page.uuid), 'subscribers': str(subscribers_count), 'posts': str(posts_count), 'likes': str(likes_count)},
                'like')
    except ObjectDoesNotExist:
        logging.error('Page does not exist')
