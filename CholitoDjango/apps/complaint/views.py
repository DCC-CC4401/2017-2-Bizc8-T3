from django.shortcuts import render, redirect
from django.views import View
from django.views.generic import TemplateView


class ListComplaintsView(TemplateView):

    template_name = 'complaint/list-complaints.html'


class StatisticsComplaintsView(TemplateView):

    template_name = 'complaint/statistics-complaints.html'


class AddComplaintView(TemplateView):

    template_name = 'complaint/add-complaint.html'
