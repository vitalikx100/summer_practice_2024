from rest_framework import serializers
from .models import City, Shop

class ShopSerializer(serializers.ModelSerializer):
    id = serializers.IntegerField(read_only=True)

    city = serializers.SerializerMethodField()
    street = serializers.SerializerMethodField()

    class Meta:
        model = Shop
        fields = ("id", "title", "building", "time_open", "time_close", "city", "street")

    def get_city(self, obj):
        return obj.city.title

    def get_street(self, obj):
        return obj.street.title


class CitySerializer(serializers.ModelSerializer):
    class Meta:
        model = City
        fields = ('id', 'title')
