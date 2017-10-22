from django.db import models

# Create your models here.
class User(models.Model):
    id = models.IntegerField()
    email = models.CharField(max_length=1000)
    password = models.CharField(max_length=1000)

    def __str__(self):
        return self.id

class Favorite(models.Model):
    user_id = models.ForeignKey(User, on_delete=models.CASCADE())
    ong_id = models.ForeignKey(ONG, on_delete=models.CASCADE())
    
class Muni(models.Model):
    id = models.IntegerField()
    name = models.CharField(max_length=1000)
    picture = models.FilePathField

    def __str__(self):
        return self.id
class ONG(models.Model):
    id = models.IntegerField()
    name = models.CharField(max_length=1000)
    picture = models.CharField(max_length=1000)
    adress = models.CharField(max_length=1000)

    def __str__(self):
        return self.id
