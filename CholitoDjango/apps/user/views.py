from django.shortcuts import render, redirect
from django.views import View
from django.views.generic import TemplateView


class LoginView(TemplateView):

    template_name = 'user/login.html'


class OngsFavoritesView(TemplateView):

    template_name = 'user/ongs-favorites.html'
