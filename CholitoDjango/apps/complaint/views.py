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
        sex = request.POST['sex']
        type_animal = request.POST['type_animal']
        hurt = request.POST['hurt']
        description = request.POST['description']
        if not complaint_check(typecomplaint, type_animal, color, sex, hurt):
            return self.get(request)
        complaint = Complaint(type=type_animal, complaintType=typecomplaint, hurt=hurt, sex=sex,
                              description=description)
        complaint.save()

        return redirect('/')


class ComplaintDetailView(View):
    def get(self, request):
        id = request.GET['id']
