from django.contrib.auth.models import User
from django import forms
from django.contrib.auth.forms import UserCreationForm


class RegistrationForm(UserCreationForm):
    email = forms.EmailField(required=True)

    class Meta:
        model = User
        fields = (
            'username',
            'first_name',
            'last_name',
            'email',
            'password1',
            'password2'
        )
    def clean_email(self):
        email= self.cleaned_data.get('email')
        username = self.cleaned_data.get('username')
        if email and User.objects.filter(email = email).exclude(username=username).exists():
            raise  forms.validationError(u'El correo ya fue usado')
        return email

    def save(self, commit=True):
        user = super(RegistrationForm, self).save(commit=False)
        user.first_name = self.cleaned_data['first_name']
        user.last_name = self.cleaned_data['last_name']
        user.email = self.cleaned_data['email']

        if commit:
            user.save()

        return user




class LogInForm(forms.Form):
    email = forms.EmailField(label='', widget=forms.EmailInput)
    password = forms.CharField(label='', widget=forms.PasswordInput)
