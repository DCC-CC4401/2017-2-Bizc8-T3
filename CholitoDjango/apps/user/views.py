from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm
from django.views.generic import CreateView, TemplateView
from django.core.urlresolvers import reverse_lazy

from apps.user.forms import RegisterForm


class LoginView(TemplateView):

    template_name = 'user/login.html'


# class RegisterView(TemplateView):

#     template_name = 'user/register.html'


class RegisterView(CreateView):
    model = User
    template_name = 'user/register.html'
    form_class = RegisterForm
    # form_class = UserCreationForm
    success_url = reverse_lazy('login')


class OngsFavoritesView(TemplateView):

    template_name = 'user/ongs-favorites.html'
