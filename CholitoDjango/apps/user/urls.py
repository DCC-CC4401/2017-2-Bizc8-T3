from django.conf.urls import url
from django.contrib.auth.decorators import login_required

from . import views

urlpatterns = [
    # url(r'^login/$', views.LoginView.as_view(), name='login'),
    url(r'^register/$', views.RegisterView.as_view(), name='register'),
    url(r'^ong-favoritas/$',
        login_required(views.OngsFavoritesView.as_view()),
        name='ongs-favorites'),
]
