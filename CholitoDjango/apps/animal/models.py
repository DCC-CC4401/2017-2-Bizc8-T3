from django.db import models

class TypeAnimal(models.Model):
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name


class Animal(models.Model):
    name = models.CharField(max_length=100, null=True, blank=True)
    type = models.ForeignKey(TypeAnimal, on_delete=models.CASCADE)
    sex = models.CharField(max_length=1)
    color = models.CharField(max_length=100)
    picture = models.CharField(max_length=100, null=True, blank=True)
    age = models.CharField(max_length=3, null=True, blank=True)
    
    def __str__(self):
        return '%s %s' % (self.name, self.color)
