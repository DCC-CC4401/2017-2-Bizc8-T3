import django.db

class TypeAnimal(django.db.models.Model):
    name = django.db.models.CharField(max_length=100)

    def __str__(self):
        return self.name


class Animal(django.db.models.Model):
    name = django.db.models.CharField(max_length=100, null=True, blank=True)
    type = django.db.models.ForeignKey(TypeAnimal, on_delete=django.db.models.CASCADE)
    sex = django.db.models.CharField(max_length=1)
    color = django.db.models.CharField(max_length=100)
    picture = django.db.models.CharField(max_length=100, null=True, blank=True)
    age = django.db.models.CharField(max_length=3, null=True, blank=True)
    
    def __str__(self):
        return '%s %s' % (self.name, self.color)
