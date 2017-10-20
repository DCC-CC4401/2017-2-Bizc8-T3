from django.conf.urls import url

from apps.complaint import views

urlpatterns = [
    url(r'^$', views.ListComplaintsView.as_view(), name='list'),
    url(r'^agregar/$', views.AddComplaintView.as_view(), name='add'),
    url(r'^estadisticas/$', views.StatisticsComplaintsView.as_view(),
        name='statistics'),
]