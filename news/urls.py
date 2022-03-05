from rest_framework import routers

from .views import CommentViewSet, NewsViewSet

router = routers.SimpleRouter()
router.register(r"news", NewsViewSet)
router.register(r"comments", CommentViewSet)

urlpatterns = router.urls
