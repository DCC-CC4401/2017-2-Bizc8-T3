from django.shortcuts import render

# Create your views here.

class AnimalsforAdoptionView(TemplateView):

    template_name = 'animal/animals-for-adoption-user.html'
    def get(self, request):
      if request.user.is_authenticated == False:
            return render(request, self.template_name)
        else:
            if request.user.typeuser.name == 'Natural':
                return render(request, self.template_name)
            elif request.user.typeuser.name == 'ONG':
                return HttpResponseRedirect(reverse('animal:list'))
      
    


class AnimalDetailView(TemplateView):

    template_name = 'animal/animal-detail.html'
    def get(self, request):
      if request.user.is_authenticated == False:
            return render(request, self.template_name)
        else:
            if request.user.typeuser.name == 'Natural':
                return render(request, self.template_name)
              
            elif request.user.typeuser.name == 'ING':
                return HttpResponseRedirect(reverse('animal:list'))
              
