from django.shortcuts import render, redirect
from django.views import View
from django.views.generic import TemplateView


class AnimalsforAdoptionView(TemplateView):
    template_name = 'animal/animals-for-adoption-user.html'


class AnimalDetailView(TemplateView):
    template_name = 'animal/animal-detail.html'


