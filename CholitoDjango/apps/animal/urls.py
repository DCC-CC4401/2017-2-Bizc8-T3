from django.conf.urls import url

from . import views

urlpatterns = [
    url(r'^ong/1/$', views.AnimalsforAdoptionView.as_view(),
        name='animals-for-adoption'),
    url(r'^animal/1/$', views.AnimalDetailView.as_view(), name='detail'),
]
