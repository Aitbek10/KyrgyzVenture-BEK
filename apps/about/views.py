from django.shortcuts import render
from .models import About

def get_about(request):
    about = About.objects.all()
    return render(request, {'about': about})