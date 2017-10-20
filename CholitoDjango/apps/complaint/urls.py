from django.conf.urls import url

from apps.complaint import views

urlpatterns = [
    url(r'^$', views.ListComplaintsView.as_view(), name='list'),
]
