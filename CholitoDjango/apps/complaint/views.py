# -*- coding: utf-8 -*-
from django.shortcuts import render, redirect
from django.views import View
from django.views.generic import TemplateView
from .models import Complaint
from .forms import *
from .utils import complaint_check


class ListComplaintsView(View):
    template_name = 'complaint/list-complaints.html'

    def get(self, request):
        complaints = Complaint.objects.all()
        context = {'complaints': complaints}

        return render(request, self.template_name, context)

    def post(self, request):
        complaints = Complaint.objects.all()
        context = {'complaints': complaints}
        return render(request, self.template_name, context)


class StatisticsComplaintsView(TemplateView):
    template_name = 'complaint/statistics-complaints.html'


class AddComplaintView(View):
    template_name = 'complaint/add-complaint.html'

    def get(self, request):
        return render(request, self.template_name)

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
    def get(self, request, pk, **kwargs):
        complaint = Complaint.objects.get(pk=pk)
        type = ["Gato", "Perro", "Loro", "Vaca", "Caballo", "Otro"]
        status = ["Reportada", "Consolidada", "Verificada", "Cerrada", "Desechada"]
        hurt = ["Sí", "No"]
        sex = ["Macho", "Hembra"]
        complaintType = ["Abandono en la calle", "Exposición a temperaturas extremas", "Falta de comida",
                         "Falta de agua", "Violencia", "Venta ambulante"]

        context = {'complaint': complaint, 'status': status, 'type': type, 'hurt': hurt, 'sex': sex,
                   'complaintType': complaintType}
        return render(request, 'complaint/complaint-detail.html', context)

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


