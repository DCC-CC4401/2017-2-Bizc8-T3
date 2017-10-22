from django.db import models

class Municipality(models.Model):
    picture = models.CharField(max_length=100)
    commune = models.CharField(max_length=100)

    def __str__(self):
        return self.commune


class ONG(models.Model):
    name = models.CharField(max_length=100)
    picture = models.CharField(max_length=100)
    commune = models.CharField(max_length=100)

    def __str__(self):
        return self.name
