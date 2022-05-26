from rest_framework.routers import DefaultRouter
from .views import UserRequestViewSet, UserRequetsGetViewSet

router = DefaultRouter()
router.register("request", UserRequestViewSet)
router.register("request-get", UserRequetsGetViewSet)
urlpatterns = router.urls
