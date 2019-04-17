from django.shortcuts import render, get_object_or_404
from django.contrib.auth.models import User, Permission
from django.contrib.auth.decorators import login_required, permission_required
from mgmnt.views import defcont
from .models import Classes, Subjects, Periods
from . import forms
from django.urls import reverse
from students.models import StudentsDB

class blnkobj(object):
    pass



def defcontst(request):
    context = defcont(request,"Academics")
    context.update({
        'academics_active': "active open",
    })
    return(context)


def home(request):
    context = defcontst(request)
    context.update({
        'msg': "Welcome To Academic Section"
    })
    return render(request, "blank.html", context)


def classaddoredit(request, id=None):
    context = defcontst(request)
    if id:
        instance = get_object_or_404(Classes, id=id)
        form = forms.Classesform(request.POST or None, instance=instance)
        context.update({
            'heading': "Edit Class",
            'bread': ["Edit Class"],
            'form': form,
        })
    else:
        form = forms.Classesform(request.POST or None)
        context.update({
            'heading': "Add Class",
            'bread': ["Add Class"],
            'form': form,
        })
    if form.is_valid():
        form.save()
        context.update({
            'msg': "Success",
        })
    return render(request, 'forms.html', context)


def class_list(request):
    devices = Classes.objects.all()
    tabledata = []

    for i in devices:
        a = blnkobj()
        a.tr1 = i.classid
        a.tr2 = i.section
        a.tr3 = i.classteacher
        a.tr4 = StudentsDB.objects.filter(classno=i).count()
        a.tr5 = Subjects.objects.filter(classno=i).count()
        a.viewurl = "#"
        a.editurl = reverse('Academic:class-edit', kwargs={'id' : i.id})
        tabledata.append(a)
    context = defcontst(request)
    context.update({
        'title' : "Class List",
        'TableHeading' : "Class List",
        'addnewurl' : reverse('Academic:class-add'),
        'bread': ['List'],
        'th1' : "Class",
        'th2' : "Secion",
        'th3' : "Class Teacher",
        'th4' : "Total Students",
        'th5' : "Total Subjects",
        'tabledata' : tabledata

    })
    return render(request, "table.html", context)


def subjectsaddoredit(request, id=None):
    context = defcontst(request)
    if id:
        instance = get_object_or_404(Subjects, id=id)
        form = forms.Subjectsform(request.POST or None, instance=instance)
        context.update({
            'heading': "Edit Subject",
            'bread': ["Edit Subject"],
            'form': form,
        })
    else:
        form = forms.Subjectsform(request.POST or None)
        context.update({
            'heading': "Add Subject",
            'bread': ["Add Subject"],
            'form': form,
        })
    if form.is_valid():
        form.save()
        context.update({
            'msg': "Success",
        })
    return render(request, 'forms.html', context)


def subjects_list(request):
    devices = Subjects.objects.all()
    tabledata = []

    for i in devices:
        a = blnkobj()
        a.tr1 = str(i.classno.classid) + "-" + str(i.classno.section)
        a.tr2 = i.periodnumber
        a.tr3 = i.subjectname
        a.tr4 = i.teacher
        a.tr5 = i.subjecttype
        a.viewurl = "#"
        a.editurl = reverse('Academic:subjects-edit', kwargs={'id' : i.id})
        tabledata.append(a)
    context = defcontst(request)
    context.update({
        'title' : "Subjects List",
        'TableHeading' : "Subjects List",
        'addnewurl' : reverse('Academic:subjects-add'),
        'bread': ['List'],
        'th1' : "Class",
        'th2' : "Period",
        'th3' : "Subject Name",
        'th4' : "Subject Teacher",
        'th5' : "Subject Type",
        'tabledata' : tabledata

    })
    return render(request, "table.html", context)


def periodaddoredit(request, id=None):
    context = defcontst(request)
    if id:
        instance = get_object_or_404(Periods, id=id)
        form = forms.Periodform(request.POST or None, instance=instance)
        context.update({
            'heading': "Edit Period",
            'bread': ["Edit Period"],
            'form': form,
        })
    else:
        form = forms.Periodform(request.POST or None)
        context.update({
            'heading': "Add Period",
            'bread': ["Add Period"],
            'form': form,
        })
    if form.is_valid():
        form.save()
        context.update({
            'msg': "Success",
        })
    return render(request, 'forms.html', context)


def period_list(request):
    devices = Periods.objects.all()
    tabledata = []

    for i in devices:
        a = blnkobj()
        a.tr1 = i.name
        a.tr2 = i.number
        a.tr3 = i.starttime
        a.tr4 = i.endtime
        a.tr5 = ""
        a.viewurl = "#"
        a.editurl = reverse('Academic:period-edit', kwargs={'id' : i.id})
        tabledata.append(a)
    context = defcontst(request)
    context.update({
        'title' : "Period List",
        'TableHeading' : "Period List",
        'addnewurl' : reverse('Academic:period-add'),
        'bread': ['List'],
        'th1' : "Name",
        'th2' : "Number",
        'th3' : "Start Time",
        'th4' : "End Time",
        'th5' : "",
        'tabledata' : tabledata

    })
    return render(request, "table.html", context)
