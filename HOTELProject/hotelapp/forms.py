from django.contrib.auth.models import User
from django import forms
from hotelapp.models import Customer
class CustomerForm(forms.ModelForm):
    class Meta:
        model = User
        fields = ['first_name', 'last_name', 'email', 'username', 'password']

class DetailsForm(forms.ModelForm):
    class Meta:
        model = Customer
        fields = "__all__"