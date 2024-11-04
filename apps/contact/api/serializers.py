from rest_framework.serializers import ModelSerializer

from apps.contact.models import Contact


class ContactSerializer(ModelSerializer):
    class Meta:
        model = Contact
        fields = [
            "id",
            "name",
            "email",
            "subject",
            "message",
            "created_at",
        ]