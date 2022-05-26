from rest_framework.routers import DefaultRouter
from .views import LibraryViewSet

router = DefaultRouter()
router.register("info", LibraryViewSet)
urlpatterns = router.urls
