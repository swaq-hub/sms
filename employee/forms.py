from django import forms
from django.forms  import ModelForm
from .models import Employeetype, employeeDB
from django.contrib.auth.models import User

class employeedb(ModelForm):
    class Meta:
        model = employeeDB
        exclude = ['userext']


class employeetype(ModelForm):
    class Meta:
        model = Employeetype
        fields = '__all__'
