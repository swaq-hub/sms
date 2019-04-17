from django import forms
from django.forms  import ModelForm
from .models import StudentsDB, AdmissionForm
from django.contrib.auth.models import User

class addoreditstudent(ModelForm):
    class Meta:
        model = StudentsDB
        exclude = ['orginfo', 'userext']




class admissionformform(ModelForm):
    class Meta:
        model = AdmissionForm
        exclude = ['formid','orginfo']