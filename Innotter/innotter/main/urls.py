from django.urls import include, path

from main.views import PageViewSet, PostViewSet, TagViewSet
from rest_framework import routers

router = routers.SimpleRouter()
router.register(r'page', PageViewSet)
router.register(r'post', PostViewSet)
router.register(r'tag', TagViewSet)

urlpatterns = router.urls