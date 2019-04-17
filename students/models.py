from django.db import models

# Create your models here.
sex_choice = (('F', 'F'), ('M', 'M'))


class StudentsDB(models.Model):
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
    orginfo = models.ForeignKey('mgmnt.Orginfo', on_delete=models.CASCADE, null=True, blank=True)
    classno = models.ForeignKey('Academic.Classes', on_delete=models.DO_NOTHING, null=True, blank=True)
    userext = models.OneToOneField('mgmnt.userextension', on_delete=models.CASCADE, null=True, blank=True)

    def __str__(self):
        return(str(self.firstname) + " " + str(self.middlename) + " " + str(self.surname) + " -- " + str(self.classno))

class Attendence(models.Model):
    student = models.ForeignKey(StudentsDB, on_delete=models.CASCADE)
    date = models.DateTimeField(auto_now=True)
    attended = models.BooleanField(default=0)


class AdmissionForm(models.Model):
    formid = models.CharField(max_length=12)
    classnumber = models.IntegerField()
    firstname = models.CharField(max_length=100)
    middlename = models.CharField(max_length=100, blank=True, null=True)
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
    lastschool = models.CharField(max_length=100)
    lastclassmarks = models.CharField(max_length=7)
    orginfo = models.ForeignKey('mgmnt.Orginfo', on_delete=models.CASCADE)