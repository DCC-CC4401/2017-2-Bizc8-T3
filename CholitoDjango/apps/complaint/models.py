import datetime

from django.db import models
from django.utils import timezone


class Complaint(models.Model):
    type = models.CharField(max_length=100)
    complaintType = models.CharField(max_length=100)
    place = models.CharField(max_length=100, default="santiago")
    hurt = models.CharField(max_length=3)
    sex = models.CharField(max_length=7)
    date = models.DateField(default=datetime.date.today,null = True)
    status = models.CharField(max_length=100, default="reportada")
    description = models.CharField(max_length=300, null=True, blank=True)
    commune = models.CharField(max_length=100)

    def __str__(self):
        return self.type


