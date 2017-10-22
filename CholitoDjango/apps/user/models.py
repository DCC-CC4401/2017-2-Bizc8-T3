from django.contrib.auth.models import User
from django.db import models
from django.utils import timezone
from django.utils.formats import get_format


class UserProfile(models.Model):
    user = models.OneToOneField(User, verbose_name='User')
    type = models.IntegerField(default=1)  # 1 natural 2 municipalidad 3 ong
    avatar = models.ImageField(default='user-avatar.png')

    def __str__(self):
        return self.user.username
    class Meta:
        verbose_name ='User'

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
