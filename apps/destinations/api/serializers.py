from rest_framework.serializers import ModelSerializer

from apps.destinations.models import Destination


class DestinationSerializer(ModelSerializer):
    class Meta:
        model = Destination
        fields = [
            "id",
            "name",
            "description",
            "image1",
            "image2",
        ]