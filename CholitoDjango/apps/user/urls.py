from django.conf.urls import url

from . import views

urlpatterns = [
    url(r'^login/$', views.LoginView.as_view(), name='login'),
    url(r'^ong-favoritas/$', views.OngsFavoritesView.as_view(),
        name='ongs-favorites'),
]
