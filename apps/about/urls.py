from django.urls import path 
from .views import get_about

urlpatterns = [ 
    path('about/', get_about, name='get_about'), 
]