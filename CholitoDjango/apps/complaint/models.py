from django.db import models
from apps.animal.models import Animal
from apps.user.models import Muni

# Create your models here.
class Complaint(models.Model):
    id = models.IntegerField()
    place = models.CharField(max_length=1000)
    type = models.CharField(max_length=1000)
    animal_id = models.ForeignKey(Animal, on_delete=models.CASCADE())
    hurt = models.BooleanField()
    date = models.DateTimeField
    municipality_id = models.ForeignKey(Muni, on_delete=models.CASCADE)
    status = models.CharField(max_length=1000)
