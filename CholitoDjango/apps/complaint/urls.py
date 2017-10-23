from django.conf.urls import url

from . import views

urlpatterns = [
    url(r'^$', views.ListComplaintsView.as_view(), name='list'),
    url(r'^agregar/$', views.AddComplaintView.as_view(), name='add'),
    url(r'^1(?P<pk>[0-9]+)/$', views.ComplaintDetailView.as_view(), name='detail'),
    url(r'^estadisticas/$', views.StatisticsComplaintsView.as_view(),
        name='statistics'),
]
