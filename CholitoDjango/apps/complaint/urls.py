from django.conf.urls import url
from django.contrib.auth.decorators import login_required

from . import views

urlpatterns = [
    url(r'^$', login_required(views.ListComplaintsView.as_view()),
        name='list'),
    url(r'^agregar/$', views.AddComplaintView.as_view(), name='add'),
    url(r'^1/$', login_required(views.ComplaintDetailView.as_view()),
        name='detail'),
    url(r'^estadisticas/$',
        login_required(views.StatisticsComplaintsView.as_view()),
        name='statistics'),
]
