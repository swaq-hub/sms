from django.db import models
from django.contrib.auth.models import User, Permission

sex_choice = (('F', 'F'), ('M', 'M'))

class Employeetype(models.Model):
    employeework = models.CharField(max_length=50)

    def __str__(self):
        return(self.employeework)

class employeeDB(models.Model):
    firstname = models.CharField(max_length=100)
    middlename = models.CharField(max_length=100, blank=True)
    surname = models.CharField(max_length=100)
    gender = models.CharField(max_length=1, choices=sex_choice)
    dateofbirth = models.DateField()
    placeofbirth = models.CharField(max_length=100)
    address = models.TextField(default="")
    phnum = models.IntegerField(default=0)
    emailid = models.CharField(max_length=100, blank=True, null=True)
    fathername = models.CharField(max_length=100)
    mothername = models.CharField(max_length=100)
    fatherprofession = models.CharField(max_length=100)
    motherprofession = models.CharField(max_length=100)
    employeetype = models.ForeignKey(Employeetype, on_delete=models.DO_NOTHING)
    image = models.ImageField(upload_to="profile_image", blank=True)
    userext = models.OneToOneField('mgmnt.userextension', on_delete=models.CASCADE, null=True, blank=True)

    def __str__(self):
        return(self.firstname + " " + self.surname)