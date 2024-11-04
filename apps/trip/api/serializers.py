# from rest_framework.serializers import ModelSerializer
from rest_framework import serializers
from apps.trip.models import Trip


class TripSerializer(serializers.ModelSerializer):
    class Meta:
        model = Trip
        fields = '__all__'