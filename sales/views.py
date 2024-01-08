from rest_framework.viewsets import ModelViewSet

from sales.models import Country, Size, SpeedIndex, WeightIndex
from sales.serializers import CountrySerializer, SizeSerializer,SpeedIndexSerializer, WeightIndexSerializer


# Create your views here.
class CountryViewSet(ModelViewSet):
    serializer_class = CountrySerializer
    queryset = Country.objects.all()


class SizeViewSet(ModelViewSet):
    serializer_class = SizeSerializer
    queryset = Size.objects.all()



class SpeedIndexViewSet(ModelViewSet):
    serializer_class = SpeedIndexSerializer
    queryset = SpeedIndex.objects.all()

class WeightIndexViewSet(ModelViewSet):
    serializer_class = WeightIndexSerializer
    queryset = WeightIndex.objects.all()