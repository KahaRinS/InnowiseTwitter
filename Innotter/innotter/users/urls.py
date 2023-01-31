from django.urls import include, path
from rest_framework import routers
from users.views import UserViewSet

router = routers.SimpleRouter()
router.register(r'user', UserViewSet, basename='user')

urlpatterns = router.urls
