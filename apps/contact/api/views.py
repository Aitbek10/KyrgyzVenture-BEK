from rest_framework.viewsets import ModelViewSet
from apps.contact.models import Contact
from apps.contact.api.serializers import ContactSerializer

class ContactApiViewSet(ModelViewSet):
    queryset = Contact.objects.all()
    serializer_class = ContactSerializer

    def get_queryset(self):
        return Contact.objects.order_by('-id')[:1]
