from rest_framework import serializers
from .models import City, Subscribe


class CitySerializer(serializers.ModelSerializer):
    class Meta:
        model = City
        fields = ['name']


class SubscribeSerializer(serializers.ModelSerializer):
    class Meta:
        model = Subscribe
        fields = ['city', 'user', 'parameter']
        read_only_fields = ['user']
