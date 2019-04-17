from django.shortcuts import render, get_object_or_404
from django.contrib.auth.models import User, Permission
from django.contrib.auth.decorators import login_required, permission_required
from mgmnt.views import defcont, send_mail2
from mgmnt.models import userextension
from Academic.models import Classes
from employee.models import employeeDB
from .models import StudentsDB, Attendence, AdmissionForm
from . import forms
from django.urls import reverse

class blnkobj(object):
    pass

# Create your views here.

def defcontst(request):
    context = defcont(request,"Student")
    context.update({
        'students_active': "active open",
    })
    return(context)


def home(request):
    context = defcontst(request)
    context.update({
        'msg': "Welcome To Student Section"
    })
    return render(request, "blank.html", context)


def studentaddoredit(request, id=None):
    context = defcontst(request)
    if id:
        instance = get_object_or_404(StudentsDB, id=id)
        form = forms.addoreditstudent(request.POST or None, request.FILES or None, instance=instance)
        context.update({
            'heading': "Edit Student",
            'bread': ["Edit Student"],
            'form': form,
        })
    else:
        form = forms.addoreditstudent(request.POST, request.FILE)
        context.update({
            'heading': "Add Student",
            'bread': ["Add Student"],
            'form': form,
        })
    if form.is_valid():
        print(form["firstname"])
        student = form.save()
        student.orginfo = userextension.objects.get(user=request.user).orginfo
        student.save()
        if not id:
            try:
                print(userextension.objects.filter(utype='student'))
                userid = str(userextension.objects.filter(utype='student').last().user)
                print(userid)
                userid = str(userid[:4]) + str(int(userid[4:userid.find("-")]) + 1) + "-S"
            except Exception as e:
                print(e)
                userid = str(userextension.objects.get(user=request.user).orginfo.shortcode) + str("1") + "-S"
            user1 = User.objects.create_user(userid, password="ChangePass")
            user1.save()
            userext = userextension(user=user1, orginfo=userextension.objects.get(user=request.user).orginfo, utype='student')
            userext.save()
            student.userext = userext
            student.save()
            emailtext = """
            Username = %s
            Password = %s
            """ % (userid, 'ChangePass')
            send_mail2('monitor.ind-cloud@everdata.com', student.emailid, "Login Details", emailtext, student.firstname)
        context.update({
            'msg': "Success",
        })
    return render(request, 'forms.html', context)


def student_list(request):
    devices = StudentsDB.objects.filter(orginfo = userextension.objects.get(user=request.user).orginfo)
    tabledata = []

    for i in devices:
        a = blnkobj()
        a.tr1 = str(i.firstname) + " " + str(i.middlename) + " " + str(i.surname)
        a.tr2 = i.gender
        a.tr3 = str(i.classno.classid) + "-" + str(i.classno.section)
        a.tr4 = i.phnum
        a.tr5 = i.dateofbirth
        a.viewurl = reverse('students:student-profile', kwargs={'id' : i.id})
        a.editurl = reverse('students:student-edit', kwargs={'id' : i.id})
        tabledata.append(a)
    context = defcontst(request)
    context.update({
        'title' : "Students List",
        'TableHeading' : "Students List",
        'addnewurl' : reverse('students:student-add'),
        'bread': ['List'],
        'th1' : "Full Name",
        'th2' : "Gender",
        'th3' : "Class",
        'th4' : "Contact",
        'th5' : "BirthDay",
        'tabledata' : tabledata

    })
    return render(request, "table.html", context)


def admissionaddoredit(request, id=None):
    context = defcontst(request)
    if id:
        instance = get_object_or_404(AdmissionForm, id=id)
        form = forms.admissionformform(request.POST or None, instance=instance)
        context.update({
            'heading': "Edit Admission Form",
            'bread': ["Edit Admission Form"],
            'form': form,
        })
    else:
        form = forms.admissionformform(request.POST or None)
        context.update({
            'heading': "Admission Form",
            'bread': ["Admission Form"],
            'form': form,
        })
    if form.is_valid():
        try:
            formid = AdmissionForm.objects.all().last().formid
            formid = str(formid[:4]) + str(int(formid[4:]) + 1)
        except:
            formid = str(userextension.objects.get(user=request.user).orginfo.shortcode) + str("1")
        form["formid"] = formid
        form["orginfo"] = userextension.objects.get(user=request.user).orginfo
        form.save()
        context.update({
            'msg': "Success",
        })
    return render(request, 'forms.html', context)


def admissionform_list(request):
    devices = AdmissionForm.objects.filter(orginfo = userextension.objects.get(user=request.user).orginfo)
    tabledata = []

    for i in devices:
        a = blnkobj(request)
        a.tr1 = str(i.firstname) + " " + str(i.middlename) + " " + str(i.surname)
        a.tr2 = i.gender
        a.tr3 = i.formid
        a.tr4 = i.phnum
        a.tr5 = i.classnumber
        a.viewurl = "#"
        a.editurl = reverse('students:admission-edit', kwargs={'id' : i.id})
        tabledata.append(a)
    context = defcontst(request)
    context.update({
        'title' : "Students List",
        'TableHeading' : "Students List",
        'addnewurl' : reverse('students:admission-add'),
        'bread': ['List'],
        'th1' : "Full Name",
        'th2' : "Gender",
        'th3' : "Form No.",
        'th4' : "Contact",
        'th5' : "Class",
        'tabledata' : tabledata

    })
    return render(request, "table.html", context)


def attendanceview(request):
    context = defcontst(request)
    studnetslist = StudentsDB.objects.filter(classno=Classes.objects.get(classteacher=employeeDB.objects.get(userext=userextension.objects.get(user=request.user))))
    if request.POST:
        for i in request.POST:
            if "csrfmiddleware" in str(i):
                pass
            else:
                Attendence(student=StudentsDB.objects.get(id=i), attended=1).save()
        context.update({
            'msg': "Success",
        })
    else:
        context = defcontst(request)
        context.update({
            'title' : "Students List",
            'addnewurl' : reverse('students:admission-add'),
            'bread': ['List'],
            'heading': "Attendance " + str(Classes.objects.get(classteacher=employeeDB.objects.get(userext=userextension.objects.get(user=request.user)))),
            'studentlist': studnetslist,
        })
    return render(request, "students/attendance.html", context)




def showstudentprofile(request,id):
    student = StudentsDB.objects.get(id=id)
    context = {
        'student' : student
    }
    return render(request, "students/profile.html", context)