from django import forms
from django.forms  import ModelForm
from .models import userextension
from django.contrib.auth.models import User

class userextensionform(ModelForm):
    first_name = forms.CharField(max_length=20)
    last_name = forms.CharField(max_length=20)
    email = forms.EmailField()
    class Meta:
        model = userextension
        fields = '__all__'

