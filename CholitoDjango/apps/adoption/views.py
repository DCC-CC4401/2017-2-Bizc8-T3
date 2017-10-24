from django.http import HttpResponseRedirect
from django.shortcuts import render
from django.views import View
from django.views.generic import TemplateView
from django.urls import reverse


class HomeView(View):
    template_name = 'adoption/home.html'

    def get(self, request):
        if request.user.is_authenticated == False:
            return render(request, self.template_name)
        else:
            if request.user.typeuser.name == 'Natural':
                return render(request, self.template_name)
            elif request.user.typeuser.name == 'Municipality':
                return HttpResponseRedirect(reverse('complaint:list'))
