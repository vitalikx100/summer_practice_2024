from rest_framework import serializers
from .models import City, Shop

class ShopSerializer(serializers.ModelSerializer):
    class Meta:
        model = Shop
        fields = ("title", "building", "time_open", "time_close", "city", "street")


class CitySerializer(serializers.ModelSerializer):
    class Meta:
        model = City
        fields = ('id', 'title')