from rest_framework.viewsets import ModelViewSet

from sales.models import Country
from sales.serializers import CountrySerializer


# Create your views here.
class CountryViewSet(ModelViewSet):
    serializer_class = CountrySerializer
    queryset = Country.objects.all()