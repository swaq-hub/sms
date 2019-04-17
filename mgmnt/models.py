from django.db import models

# Create your models here.
from django.db import models
from django.contrib.auth.models import User, Permission



gender_choice = (('M', 'M'), ('F', 'F'))
usertypechoice = (('admin', 'admin'), ('user','user'))
# Create your models here.

class Orginfo(models.Model):
    name = models.CharField(max_length=100, default="Solve The Network")
    address = models.TextField(default="")
    phnum = models.IntegerField(default=0)
    emailid = models.CharField(max_length=100, default="info@solvethenetwork.com")
    orgurl = models.URLField(default="https://solvethenetwork.com")
    chkinfo = models.TextField()
    shortcode = models.CharField(max_length=5)

    def __str__(self):
        return (self.name)

class userextension(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    orginfo = models.ForeignKey(Orginfo, on_delete=models.CASCADE)
    utype = models.CharField(max_length=10, default="employee")
    def __str__(self):
        return (self.user.username)


