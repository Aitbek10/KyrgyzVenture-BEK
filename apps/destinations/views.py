from django.http import JsonResponse
from .models import Destination

def get_destinations(request):
    destinations = Destination.objects.all()
    data = [
        {
            'name': destination.name,
            'description': destination.description,
            'image1': destination.image1.url if destination.image1 else None,
            'image2': destination.image2.url if destination.image2 else None,
        }
        for destination in destinations
    ]
    return JsonResponse(data, safe=False)
