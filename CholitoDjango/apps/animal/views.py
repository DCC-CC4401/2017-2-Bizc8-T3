from django.shortcuts import render, redirect
from django.views import View
from django.views.generic import TemplateView
from .models import *
from .utils import adopt


class AnimalsforAdoptionView(View):
    template_name = 'animal/animals-for-adoption-user.html'

    def get(self, request):
            animals = Animal.objects.all()
            context = {'animals': animals}
            return render(request, self.template_name, context)




class AnimalDetailView(View):
    template_name = 'animal/animal-detail.html'

    def post(self, request):
        if request.user.is_authenticated == False:
            return redirect('/')
        else:
            id =request.POST['id']
            adoption = request.POST['adoption']
            if adoption == "NO":
                animal = Animal.objects.get(id=id)
                context = {'animal':animal}
                return render(request,self.template_name,context)
            else:

                adopt(id,request.user.id)
                return redirect('../../ong/1/')
