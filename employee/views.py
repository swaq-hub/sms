from django.shortcuts import render, get_object_or_404
from django.contrib.auth.models import User, Permission
from django.contrib.auth.decorators import login_required, permission_required
from mgmnt.views import defcont, send_mail2
from .models import employeeDB, Employeetype
from mgmnt.models import userextension
from . import forms
from django.urls import reverse

class blnkobj(object):
    pass

# Create your views here.

def defcontst(request):
    context = defcont(request,"Employee")
    context.update({
        'employee_active': "active open",
    })
    return(context)


def home(request):
    context = defcontst(request)
    context.update({
        'msg': "Welcome To Employee Section"
    })
    return render(request, "blank.html", context)


def employeeaddoredit(request, id=None):
    context = defcontst(request)
    if id:
        instance = get_object_or_404(employeeDB, id=id)
        form = forms.employeedb(request.POST or None, instance=instance)
        context.update({
            'heading': "Edit Employee",
            'bread': ["Edit Employee"],
            'form': form,
        })
    else:
        form = forms.employeedb(request.POST or None)
        context.update({
            'heading': "Add Employee",
            'bread': ["Add Employee"],
            'form': form,
        })
    if form.is_valid():
        emp = form.save()
        if not id:
            try:
                print(userextension.objects.filter(utype='employee'))
                userid = str(userextension.objects.filter(utype='employee').last().user)
                print(userid)
                userid = str(userid[:4]) + str(int(userid[4:userid.find("-")]) + 1) + "-T"
            except Exception as e:
                print(e)
                userid = str(userextension.objects.get(user=request.user).orginfo.shortcode) + str("1") + "-T"
            user1 = User.objects.create_user(userid, password="ChangePass")
            user1.save()
            userext = userextension(user=user1, orginfo=userextension.objects.get(user=request.user).orginfo)
            userext.save()
            emp.userext = userext
            emp.save()
            emailtext = """
            Username = %s
            Password = %s
            """ % (userid, 'ChangePass')
            send_mail2('monitor.ind-cloud@everdata.com', emp.emailid, "Login Details", emailtext, emp.firstname)
        context.update({
            'msg': "Success",
        })
    return render(request, 'forms.html', context)


def employee_list(request):
    devices = employeeDB.objects.all()
    tabledata = []

    for i in devices:
        a = blnkobj()
        a.tr1 = str(i.firstname) + " " + str(i.middlename) + " " + str(i.surname)
        a.tr2 = i.gender
        a.tr3 = i.employeetype
        a.tr4 = i.phnum
        a.tr5 = i.dateofbirth
        a.viewurl = "#"
        a.editurl = reverse('employee:employee-edit', kwargs={'id' : i.id})
        tabledata.append(a)
    context = defcontst(request)
    context.update({
        'title' : "Employee List",
        'TableHeading' : "Employee List",
        'addnewurl' : reverse('employee:employee-add'),
        'bread': ['List'],
        'th1' : "Full Name",
        'th2' : "Gender",
        'th3' : "Type",
        'th4' : "Contact",
        'th5' : "BirthDay",
        'tabledata' : tabledata

    })
    return render(request, "table.html", context)


def employeetypeaddoredit(request, id=None):
    context = defcontst(request)
    if id:
        instance = get_object_or_404(employeeDB, id=id)
        form = forms.employeetype(request.POST or None, instance=instance)
        context.update({
            'heading': "Edit Employee",
            'bread': ["Edit Employee"],
            'form': form,
        })
    else:
        form = forms.employeetype(request.POST or None)
        context.update({
            'heading': "Add Employee",
            'bread': ["Add Employee"],
            'form': form,
        })
    if form.is_valid():
        form.save()
        context.update({
            'msg': "Success",
        })
    return render(request, 'forms.html', context)


def employeetype_list(request):
    devices = Employeetype.objects.all()
    tabledata = []

    for i in devices:
        a = blnkobj()
        a.tr1 = i.employeework
        a.tr2 = employeeDB.objects.filter(employeetype=i).count()
        a.tr3 = ""
        a.tr4 = ""
        a.tr5 = ""
        a.viewurl = "#"
        a.editurl = reverse('employee:employeetype-edit', kwargs={'id' : i.id})
        tabledata.append(a)
    context = defcontst(request)
    context.update({
        'title' : "Employee List",
        'TableHeading' : "Employee List",
        'addnewurl' : reverse('employee:employeetype-add'),
        'bread': ['List'],
        'th1' : "employeework",
        'th2' : "Total Employee",
        'th3' : "",
        'th4' : "",
        'th5' : "",
        'tabledata' : tabledata

    })
    return render(request, "table.html", context)

