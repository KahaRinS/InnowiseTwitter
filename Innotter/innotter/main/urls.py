from django.urls import include, path

from main.views import PageViewSet, PostViewSet, TagViewSet, NewsViewSet
from rest_framework import routers

router = routers.SimpleRouter()
router.register(r'page', PageViewSet)
router.register(r'post', PostViewSet)
router.register(r'tag', TagViewSet)
router.register(r'news', NewsViewSet)

urlpatterns = router.urls