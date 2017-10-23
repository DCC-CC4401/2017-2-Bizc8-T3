from django.conf.urls import url
from django.contrib.auth.decorators import login_required

from . import views

urlpatterns = [
    url(r'^$', login_required(views.list_complaints),
        name='list'),
    url(r'^agregar/$', views.add_complaint, name='add'),
    url(r'^1/$', login_required(views.complaint_detail),
        name='detail'),
    url(r'^estadisticas/$',
        login_required(views.statistics_complaints),
        name='statistics'),
]
