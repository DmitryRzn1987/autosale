from rest_framework import serializers

from sales.models import Country


class CountrySerializer(serializers.ModelSerializer):
    class Meta:
        model=Country
        fields = '__all__'