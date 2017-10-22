from django.db import models

# Create your models here.
class Adoption(models.Model):
    id = models.IntegerField()
    animal_id = models.ForeignKey(Animal, on_delete=models.CASCADE())
    ong_id = models.ForeignKey(ONG, on_delete=models.CASCADE())
    arrival = models.DateTimeField
    departure = models.DateTimeField(null=True, blank=True)
    user_id = models.ForeignKey(User, on_delete=models.CASCADE(), null=True, blank=True)
