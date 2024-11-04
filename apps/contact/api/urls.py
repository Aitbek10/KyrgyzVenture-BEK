from rest_framework.routers import DefaultRouter

from apps.contact.api.views import ContactApiViewSet

router = DefaultRouter()
router.register(
    r'contact',
    ContactApiViewSet
)

urlpatterns = router.urls