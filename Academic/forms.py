from django import forms
from django.forms  import ModelForm
from .models import Classes, Subjects, Session, Periods
from django.contrib.auth.models import User

class Classesform(ModelForm):
    class Meta:
        model = Classes
        fields = '__all__'


class Subjectsform(ModelForm):
    class Meta:
        model = Subjects
        fields = '__all__'


class Sessionform(ModelForm):
    class Meta:
        model = Session
        fields = '__all__'


class Periodform(ModelForm):
    class Meta:
        model = Periods
        fields = '__all__'