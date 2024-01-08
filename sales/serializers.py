from rest_framework import serializers

from sales.models import Country, Size, SpeedIndex, WeightIndex


class CountrySerializer(serializers.ModelSerializer):
    class Meta:
        model = Country
        fields = '__all__'


class SizeSerializer(serializers.ModelSerializer):
    class Meta:
        model = Size
        fields = '__all__'


class SpeedIndexSerializer(serializers.ModelSerializer):
    class Meta:
        model = SpeedIndex
        field = '__all__'


class WeightIndexSerializer(serializers.ModelSerializer):
    class Meta:
        model: WeightIndex
        field = '__all__'
