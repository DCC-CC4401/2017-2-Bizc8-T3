from .models import *
from django.contrib.auth.models import User

def create_user(form):
    print("--------")
    user = User.objects.create_user(username=form.cleaned_data['name'],
                                    email=form.cleaned_data['email'],password=form.cleaned_data['password'])
    usernew = User(user=user)
    user.save()
