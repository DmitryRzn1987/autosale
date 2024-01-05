from rest_framework.routers import SimpleRouter
from .views import CountryViewSet

router=SimpleRouter()
router.register('countries',CountryViewSet,basename='countries')

urlpatterns_sales = []

urlpatterns_sales +=router.urls