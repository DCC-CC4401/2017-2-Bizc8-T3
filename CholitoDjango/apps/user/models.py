from django.db import models
from django.contrib.auth.models import User
from django.db.models.signals import post_save
from django.dispatch import receiver


class Municipality(models.Model):
    user = models.OneToOneField(User)
    picture = models.CharField(max_length=100)
    commune = models.CharField(max_length=100)

    def __str__(self):
        return self.commune


class ONG(models.Model):
    user = models.OneToOneField(User)
    name = models.CharField(max_length=100)
    picture = models.CharField(max_length=100)
    commune = models.CharField(max_length=100)

    def __str__(self):
        return self.name


class TypeUser(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    name = models.CharField(max_length=100, default='Natural')

 
@receiver(post_save, sender=User)
def create_user_typeuser(sender, instance, created, **kwargs):
    if created:
        TypeUser.objects.create(user=instance)


@receiver(post_save, sender=User)
def save_user_typeuser(sender, instance, **kwargs):
    instance.typeuser.save()
