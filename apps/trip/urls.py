from django.urls import path 
from .views import get_trip

urlpatterns = [ 
    path('trip/', get_trip, name='get_trip'), 
]
