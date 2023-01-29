from django.urls import include, path
from rest_framework import routers
from users.views import UserViewSet

router = routers.SimpleRouter()
router.register(r'user', UserViewSet)

urlpatterns = router.urls
