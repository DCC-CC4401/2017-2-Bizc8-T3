from django import forms


class AddComplaint(forms.Form):
    type_complaint = forms.CharField(max_length=100)
    type_animal = forms.CharField(max_length=10)
    color = forms.CharField(max_length=50)
    sex = forms.CharField(max_length=3)
    hurt = forms.CharField(max_length=3)
    description = forms.CharField(max_length=100)
