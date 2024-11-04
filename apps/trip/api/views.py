from rest_framework.viewsets import ModelViewSet
from apps.trip.models import Trip
from apps.trip.api.serializers import TripSerializer


class TripApiViewSet(ModelViewSet):
    queryset = Trip.objects.all()
    serializer_class = TripSerializer