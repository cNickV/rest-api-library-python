from rest_framework.routers import DefaultRouter
from .views import LibraryViewSet

router = DefaultRouter()
router.register("catalog", LibraryViewSet)
urlpatterns = router.urls
