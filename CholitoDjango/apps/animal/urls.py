from django.conf.urls import url

from . import views

urlpatterns = [
    url(r'^ong/1/$', views.AnimalsforAdoptionView.as_view(),
        name='animals-for-adoption'),
]
