from main.views import NewsViewSet, PageViewSet, PostViewSet, TagViewSet
from rest_framework import routers

router = routers.SimpleRouter()
router.register(r'page', PageViewSet)
router.register(r'post', PostViewSet)
router.register(r'tag', TagViewSet)
router.register(r'news', NewsViewSet)

urlpatterns = router.urls
