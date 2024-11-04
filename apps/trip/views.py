from django.shortcuts import render
from .models import Trip 

def get_trip(request):
    trip = Trip.objects.all()
    return render(request, {'trip': trip})