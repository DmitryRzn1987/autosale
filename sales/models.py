from django.db import models

class Country(models.Model):
    name = models.CharField(max_length=255, unique=True)

class Size(models.Model):
    size = models.CharField(max_length=255, unique=True)


class SpeedIndex(models.Model):
    value = models.CharField(max_length=255, unique=True)

class WeightIndex(models.Model):
    value = models.CharField(max_length=255, unique=True)

class Manufacturer(models.Model):
    name = models.CharField(max_length=255)
    country = models.ForeignKey(Country, on_delete=models.DO_NOTHING)
    class Meta:
        unique_together = ['name','country']

class Tire(models.Model):
    name = models.CharField(max_length=255)
    year = models.IntegerField()
    size = models.ForeignKey(Size, on_delete=models.DO_NOTHING)
    manufacturer = models.ForeignKey(Manufacturer, on_delete=models.DO_NOTHING)
    speed_index = models.ForeignKey(SpeedIndex, on_delete=models.DO_NOTHING)
    weight_index = models.ForeignKey(WeightIndex, on_delete=models.DO_NOTHING)