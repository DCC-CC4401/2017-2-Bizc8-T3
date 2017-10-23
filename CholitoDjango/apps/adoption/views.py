from django.http import HttpResponseRedirect
from django.shortcuts import render
from django.views import View
from django.views.generic import TemplateView
from django.urls import reverse


def home(request):
    if request.user.is_authenticated == False:
        return render(request, 'adoption/home.html')
    else:
        if request.user.typeuser.name == 'Natural':
            return render(request, 'adoption/home.html')
        elif request.user.typeuser.name == 'Municipality':
            return HttpResponseRedirect(reverse('complaint:list'))

