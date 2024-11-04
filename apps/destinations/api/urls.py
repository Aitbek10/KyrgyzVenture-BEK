from rest_framework.routers import DefaultRouter

from apps.destinations.api.views import DestinationApiViewSet

router = DefaultRouter()
router.register(
    r'destinations',
    DestinationApiViewSet
)

urlpatterns = router.urls