from rest_framework import serializers
from ..models import About

class AboutSerializer(serializers.ModelSerializer):
    class Meta:
        model = About
        fields = ['id', 'history', 'mission', 'vision']
