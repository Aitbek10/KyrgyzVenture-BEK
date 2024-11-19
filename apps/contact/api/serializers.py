from rest_framework.serializers import ModelSerializer
from apps.contact.models import Contact

class ContactSerializer(ModelSerializer):
    class Meta:
        model = Contact
        fields = [
            "address",
            "phone1",
            "phone2",
            "email",
            "facebook",
            "instagram",
        ]
