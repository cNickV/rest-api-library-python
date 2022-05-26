from rest_framework.routers import DefaultRouter
from .views import ShelfViewSet

router = DefaultRouter()
router.register("shelfs-info", ShelfViewSet)
urlpatterns = router.urls
