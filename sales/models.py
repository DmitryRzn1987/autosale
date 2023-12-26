from django.db import models

class Model(models.Model):

    car_title = models.CharField(max_length=255)
    state = models.CharField(max_length=100)
    city = models.CharField(max_length=100)
    color = models.CharField(max_length=100)
    model = models.CharField(max_length=100)
    year = models.IntegerField()
    condition = models.CharField(max_length=100)
    price = models.IntegerField()

    def __str__(self):
        return self.car_title

