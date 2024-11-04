from rest_framework.viewsets import ModelViewSet

from apps.destinations.models import Destination
from apps.destinations.api.serializers import DestinationSerializer


class DestinationApiViewSet(ModelViewSet):
    queryset = Destination.objects.all()
    serializer_class = DestinationSerializer
