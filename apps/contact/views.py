from django.shortcuts import render
from .models import Contact

def get_contact(request):
    contact = Contact.objects.all()
    return render(request, {'contact': contact})