from django.conf.urls import url
from . import views
from django.contrib.auth.views import login

urlpatterns = [
    url(r'^login/$', views.Login.as_view(), name='login'),
    url(r'^register/$', views.SignUp.as_view(), name='sign-up'),
    url(r'^natural/$', views.LogNaturalView.as_view(), name='natural-log'),

    url(r'^ong-favoritas/$', views.OngsFavoritesView.as_view(),
        name='ongs-favorites'),

]
