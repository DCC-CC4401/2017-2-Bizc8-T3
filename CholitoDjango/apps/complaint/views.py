from django.http import HttpResponseRedirect
from django.shortcuts import render, redirect
from django.views import View
from django.views.generic import TemplateView
from django.urls import reverse
from .models import Complaint

class ListComplaintsView(View):
    template_name = 'complaint/list-complaints.html'

    def get(self, request):
        if request.user.typeuser.name != 'Municipality':
            return HttpResponseRedirect(reverse('adoption:home'))
        else:
            return render(request, self.template_name)
    
    def post(self, request):
        complaints = Complaint.objects.all()
        context = {'complaints': complaints}
        return render(request, self.template_name, context)

class StatisticsComplaintsView(View):
    template_name = 'complaint/statistics-complaints.html'

    def get(self, request):
        if request.user.typeuser.name != 'Municipality':
            return HttpResponseRedirect(reverse('adoption:home'))
        else:
            return render(request, self.template_name)

class AddComplaintView(View):
    template_name = 'complaint/add-complaint.html'

    def get(self, request):
        if request.user.is_authenticated == False:
            return render(request, 'complaint/add-complaint.html')
        else:
            if request.user.typeuser.name == 'Natural':
                return render(request, 'complaint/add-complaint.html')
            elif request.user.typeuser.name == 'Municipality':
                return HttpResponseRedirect(reverse('complaint:list'))

    def post(self, request):
        typecomplaint = request.POST['type_complaint']
        color = request.POST['color']
        type_animal = request.POST['type_animal']
        description = request.POST['description']
        if not complaint_check(typecomplaint, type_animal, color):
            return self.get(request)

        hurt = request.POST['hurt']
        sex = request.POST['sex']
        complaint = Complaint(type=type_animal, complaintType=typecomplaint, hurt=hurt, sex=sex,
                              description=description,color=color)
        complaint.save()

        return redirect('/')


class ComplaintDetailView(View):
    template_name = 'complaint/complaint-detail.html'

    def get(self, request):
        if request.user.typeuser.name != 'Municipality':
            return HttpResponseRedirect(reverse('adoption:home'))
        else:
            return render(request, self.template_name)

    def post(self,request,**kwargs):
        id = request.POST['id']
        complaint = Complaint.objects.get(id =id)
        complaint.status = request.POST['status']
        complaint.complaintType = request.POST['type_complaint']
        complaint.type = request.POST['type_animal']
        complaint.hurt =request.POST['hurt']
        complaint.sex = request.POST['sex']
        complaint.description = request.POST['description']
        complaint.color = request.POST['color']

        complaint.save()
        return redirect('/denuncias')
