from django.db import models

# Create your models here.
class Animal(models.Model):
    id = models.IntegerField()
    color = models.CharField(max_length=1000)
    name = models.CharField(max_length=1000, null=True, blank=True)
    type= models.ForeignKey(Type_Animal, on_delete=models.CASCADE())
    picture = models.CharField(max_length=1000, null=True, blank=True)
    sex = models.CharField(max_length=1000)
    age = models.IntegerField(null=True, blank=True)

    def __str__(self):
        return self.id




class Type_Animal(models.Model):
    id = models.IntegerField()
    name = models.CharField(max_length=1000)

    def __str__(self):
        return self.name
