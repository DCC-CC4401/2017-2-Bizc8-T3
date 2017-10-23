import django.db
import datetime


class TypeAnimal(django.db.models.Model):
    name = django.db.models.CharField(max_length=100)

    def __str__(self):
        return self.name


class Animal(django.db.models.Model):
    name = django.db.models.CharField(max_length=100, null=True, blank=True)
    type = django.db.models.ForeignKey(TypeAnimal, on_delete=django.db.models.CASCADE)
    sex = django.db.models.CharField(max_length=10)
    color = django.db.models.CharField(max_length=100)
    picture = django.db.models.ImageField(upload_to='static/img/')
    age = django.db.models.CharField(max_length=3, null=True, blank=True)
    arrival = django.db.models.DateField(default=datetime.date.today, null=True)
    adopted = django.db.models.BooleanField(default=False)

    def __str__(self):
        return '%s %s' % (self.name, self.color)
