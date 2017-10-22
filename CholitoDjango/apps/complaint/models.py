import datetime

from django.db import models
from django.utils import timezone

from apps import animal

class Municipality(models.Model):
    picture = models.CharField(max_length=100)
    commune = models.CharField(max_length=100)

    def __str__(self):
        return self.commune


class Complaint(models.Model):
    type = models.CharField(max_length=100)
    animal_id = models.ForeignKey(animal.models.Animal, on_delete=models.CASCADE)
    hurt = models.CharField(max_length=1)
    date = models.DateTimeField('date published')
    status = models.CharField(max_length=100)
    description = models.CharField(max_length=300, null=True, blank=True)
    commune = models.CharField(max_length=100)

    def __str__(self):
        return self.type
