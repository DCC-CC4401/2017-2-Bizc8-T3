from django.http import HttpResponseRedirect
from django.shortcuts import render
from django.views import View
from django.views.generic import TemplateView
from django.urls import reverse


def list_complaints(request):
    if request.user.typeuser.name != 'Municipality':
        return HttpResponseRedirect(reverse('adoption:home'))
    else:
        return render(request, 'complaint/list-complaints.html')


def statistics_complaints(request):
    if request.user.typeuser.name != 'Municipality':
        return HttpResponseRedirect(reverse('adoption:home'))
    else:
        return render(request, 'complaint/statistics-complaints.html')


def add_complaint(request):
    if request.user.is_authenticated == False:
        return render(request, 'complaint/add-complaint.html')
    else:
        if request.user.typeuser.name == 'Natural':
            return render(request, 'complaint/add-complaint.html')
        elif request.user.typeuser.name == 'Municipality':
            return HttpResponseRedirect(reverse('complaint:list'))


def complaint_detail(request):
    if request.user.typeuser.name != 'Municipality':
        return HttpResponseRedirect(reverse('adoption:home'))
    else:
        return render(request, 'complaint/complaint-detail.html')
