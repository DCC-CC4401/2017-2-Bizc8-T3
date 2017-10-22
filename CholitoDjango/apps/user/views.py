from django.shortcuts import render, redirect
from django.views import View
from django.contrib import auth
from django.contrib.auth import authenticate, login
from django.urls import reverse
from django.views.generic import TemplateView
from . import utils
from .forms import *


def index(request):
    return render(request, 'user/index.html')





class OngsFavoritesView(TemplateView):
    template_name = 'user/ongs-favorites.html'


class SignUp(View):
    def get(self, request):
        form = RegistrationForm()
        return render(request, 'user/register.html', {'form': form})

    def post(self, request):
        form = RegistrationForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect(reverse('user/login/'))

        else:
            form = RegistrationForm()

            args = {'form': form}
        return render(request, 'user/signup.html', args)


class Login(View):
    def get(sefl, request):
        form = LogInForm()
        return render(request, 'user/login.html', {'form': form})

    def post(self, request):
        form = LogInForm(request.POST)
        if not form.is_valid():
            self.get(request)
        email = request.POST['email']
        email=email.lower()
        password = request.POST['password']
        username = User.objects.get(email=email)
        user = authenticate(username=username.username, password=password)
        if user is None:
            return render(request, 'user/login.html', {'error': 'Usuario o contrasena invalidos', 'form': form, })
        if user.is_active:
            auth.login(request, user)
            userop = User.objects.get(user=user)
            type = userop.type
            if type == 1:  # natural

                return redirect('natural-user')
            elif type == 2:  # municipal
                return redirect('municipal_index')
        else:
            return redirect('ong_index')
        return render(request, 'user/login.html', {'form': form})
