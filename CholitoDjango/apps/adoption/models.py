import datetime

from django.db import models
from django.utils import timezone
from .apps.animal.models import Animal
from .apps.user.models import ONG


class Adoption(models.Model):
    animal_id = models.ForeignKey(Animal, on_delete=models.CASCADE)
    ong_id = models.ForeignKey(ONG, on_delete=models.CASCADE)
    arrival = models.DateTimeField()
    departure = models.DateTimeField(null=True, blank=True)

    def __str__(self):
        return self.arrival
