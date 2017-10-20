from django.conf.urls import url

from apps.adoption import views

urlpatterns = [
    url(r'^$', views.HomeView.as_view(), name='home'),
]
