import datetime

from django.db import models
from django.utils import timezone

from apps.animal.models import Animal

class ONG(models.Model):
    name = models.CharField(max_length=100)
    picture = models.CharField(max_length=100)
    commune = models.CharField(max_length=100)

    def __str__(self):
        return self.name


class Adoption(models.Model):
    animal_id = models.ForeignKey(Animal, on_delete=models.CASCADE)
    ong_id = models.ForeignKey(ONG, on_delete=models.CASCADE)
    arrival = models.DateTimeField()
    departure = models.DateTimeField(null=True, blank=True)

    def __str__(self):
        return self.arrival
