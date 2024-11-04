# from django.urls import path, include
# from rest_framework.routers import DefaultRouter
# from .views import AboutViewSet

# router = DefaultRouter()
# router.register(r'about', AboutViewSet)

# urlpatterns = [
#     path('api/', include(router.urls)),  # Убедитесь, что путь правильный
# ]

# apps/about/api/urls.py
from django.urls import path
from .views import AboutViewSet  # Импортируйте get_about, если нужно

urlpatterns = [
    path('about/', AboutViewSet.as_view({'get': 'list'}), name='get_about'),  # Если используете ViewSet
    # path('about/', get_about, name='get_about'),  # Для простого представления
]
