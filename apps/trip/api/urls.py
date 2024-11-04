# from rest_framework.routers import DefaultRouter

# from apps.trip.api.views import TripApiViewSet

# router = DefaultRouter()
# router.register(
#     r'trip',
#     TripApiViewSet
# )

# urlpatterns = router.urls

# apps/trip/api/urls.py
from rest_framework.routers import DefaultRouter
from apps.trip.api.views import TripApiViewSet

router = DefaultRouter()
router.register(r'trip', TripApiViewSet)

urlpatterns = router.urls
