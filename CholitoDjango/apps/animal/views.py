from django.http import HttpResponseRedirect
from django.shortcuts import render
from django.views import View
from django.urls import reverse
from apps.adoption.models import Adoption
from apps.animal.models import Animal


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
            return HttpResponseRedirect(reverse('animal:animals-for-adoption'))
        elif request.user.typeuser.name != 'Natural':
            return HttpResponseRedirect(reverse('animal:animals-for-adoption'))
        else:
            id = request.POST['id']
            adoption = request.POST['adoption']
            if adoption == "NO":
                animal = Animal.objects.get(id=id)
                context = {'animal':animal}
                return render(request, self.template_name, context)
            else:
                adoption = Adoption(animal_id=id, person_id=request.user.id)
                adoption.save()
                return HttpResponseRedirect(reverse('animal:animals-for-adoption'))
