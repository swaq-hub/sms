from django.db import models

# Create your models here.
class Session(models.Model):
    startdate = models.DateField()
    enddate = models.DateField()

    def __str__(self):
        return(str(self.startdate) + " - " + str(self.enddate))


class Classes(models.Model):
    classid = models.IntegerField()
    section = models.CharField(max_length=2)
    classteacher = models.ForeignKey('employee.employeeDB', on_delete=models.DO_NOTHING)

    def __str__(self):
        return (str(self.classid) + " " + str(self.section))


class Periods(models.Model):
    name = models.CharField(max_length=20)
    number = models.IntegerField()
    starttime = models.TimeField()
    endtime = models.TimeField()

    def __str__(self):
        return(self.name + " " + str(self.starttime) + " " + str(self.endtime))


subtypechoice = [('Primary','Primary'),('Aditional','Aditional')]
class Subjects(models.Model):
    subjectname = models.CharField(max_length=50)
    subjecttype = models.CharField(max_length=10, choices=subtypechoice)

    def __str__(self):
        return(self.subjectname)

class subjectallocat(models.Model):
    subjectid = models.ForeignKey(Subjects, on_delete=models.CASCADE)
    classno = models.ForeignKey(Classes, on_delete=models.CASCADE)
    periodnumber = models.ForeignKey(Periods, on_delete=models.DO_NOTHING)
    teacher = models.ForeignKey('employee.employeeDB', on_delete=models.DO_NOTHING)



class examsschedule(models.Model):
    subjectid = models.ForeignKey(Subjects, on_delete=models.DO_NOTHING)
    schedule = models.DateTimeField()

