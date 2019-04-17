from django.shortcuts import render, get_object_or_404
from .models import Orginfo, userextension
from django.contrib.auth.forms import UserCreationForm, PasswordChangeForm
from .forms import userextensionform
from django.contrib.auth.models import User, Permission
from django.contrib.auth.decorators import login_required, permission_required
import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.application import MIMEApplication
from email.mime.text import MIMEText
from email.utils import formatdate
import mimetypes
from os.path import basename
import email.utils




#@todo https://12202908-a-62cb3a1a-s-sites.googlegroups.com/site/bcafinalyearproject/project-report/school-management-system-project-report/er-diagram-of-school-management-system/ER%20DIAGRAM%20OF%20SCHOOL%20MANAGEMENT%20SYSTEM%20PROJECT%20REPORT.jpg?attachauth=ANoY7cpmREkF-Y-7KsIG1G3gxKZbL5yhV0H7i5Sg1aXj3p5f9islI4_tVpt9d3a4yIf4EJHxHvTOgfR9nGAJhbdpmJI1iFS_Cli-U3_2MbMHL3CF9mb8WFUppNCd0DOGZYx58NCdsS_efiFAHkK2zEIldnWsm8Y4EGRapt0xgNqa9_VF7VN5Vh1v4jtJAmHSriLD_Q0hcp7Q90vJo1cHMBixshc8QIiNidP2FANI6Zbw892prhUWEf3xASwHofvqUPggzNxO9crwibsXI_E-X8W5Rm17-M1TJ3Wf03VcDeS5lPbaJYhFxtd20qj65sRCQ60OW4cwxnRa-7MHO2-z3Dd88Y63bXUM66d7drBJN6ycY-gvkL93xCO6Dw7f_0x_g_lbcwM29snCI9x98ci-P7k96-jDeCkwsA%3D%3D&attredirects=0
#@todo https://i.stack.imgur.com/gUAbT.jpg



class blnkobj(object):
    pass


def defcont(request,app_name):
    orgdetails = userextension.objects.get(user=request.user).orginfo
    context = {
        'title': str(orgdetails.name) + " " + "Management System",
        'orgname': orgdetails.name,
        'orgurl' : "$",
        'dashboard_active': "",
        'inventory_active': "",
        'device_management_active': "",
        'app_name': app_name,
    }
    return (context)


def home(request):
    context = defcont(request,"Admin")
    context.update({
        'msg': "Welcome To Inventory Section"
    })
    return render(request, "blank.html", context)

@permission_required('User.can_add_user' and 'User.can_edit_user')
def userregistration(request):
    context = defcont(request,'Admin')
    form = UserCreationForm(request.POST or None)
    context.update({
        'heading': "Add User",
        'bread': ["Add User"],
        'form': form,
    })
    if request.POST:
        if form.is_valid():
            form.save()
            permission_name = ["Can add task_ commands",
                               "Can change task_ commands",
                               "Can add tasks",
                               "Can change tasks",
                               "Can add devices",
                               "Can change devices",
                               "Can add devices type",
                               "Can change devices type",
                               "Can add aaauserdb",
                               "Can change aaauserdb",
                               ]
            u = User.objects.get(username=form.cleaned_data['username'])
            for i in permission_name:
                u.user_permissions.add(Permission.objects.get(name=i))
            context.update({
                'msg': "Success",
            })
    return render(request, 'forms.html', context)

def userlist(request):
    context = defcont(request,"Admin")
    users = User.objects.all()
    context.update({
        'heading': "Add User",
        'bread': ["Add User"],
        'users': users
    })
    return render(request, 'mgmnt/users.html', context)

@permission_required('User.can_delete_user')
def deluser(request,id):
    context = defcont(request,'Admin')
    userd = User.objects.get(id=id)
    userd.delete()
    context.update({
        'msg': "Success",
    })
    return render(request, 'forms.html', context)


def userprofile(request):
    context = defcont(request,'Admin')
    return render(request, 'mgmnt/profile.html', context)


def edituserprofile(request):
    context = defcont(request,'Admin')
    user = request.user
    instance = get_object_or_404(userextension, user=user)
    userinitial = {
        'first_name' : user.first_name,
        'last_name' : user.last_name,
        'email' : user.email
    }
    userexteform = userextensionform(request.POST or None, request.FILES or None, instance=instance or None, initial=userinitial)
    context.update({
        'userexteform' : userexteform,
        'pchangeform' : PasswordChangeForm(request.user, request.POST or None)
    })
    if request.POST:
        if userexteform.is_valid():
            userexteform.save()
            user.first_name = userexteform.cleaned_data['first_name']
            user.last_name = userexteform.cleaned_data['last_name']
            user.email = userexteform.cleaned_data['email']
            user.save()
    return render(request, 'mgmnt/profile-settings.html', context)


def passwordchange(request):
    context = defcont(request,'Admin')
    pchangeform = PasswordChangeForm(request.user, request.POST or None)
    context.update({
        'form' : pchangeform
    })
    if request.POST:
        if pchangeform.is_valid():
            pchangeform.save()
            context.update({
                'msg' : "Password Changed successfully"
            })
    return render(request, 'forms.html', context)




def send_mail2(send_from, send_to, subject, text, cname):
    msg = MIMEMultipart()
    msg['From'] = email.utils.formataddr(("School Management", send_from))
    msg['To'] = email.utils.formataddr((cname, send_to))
    msg['Date'] = formatdate(localtime=True)
    msg['Subject'] = subject
    msg['Reply-to'] = send_from
    msg.attach(MIMEText(text))
    server = smtplib.SMTP("mail.solvethenetwork.com")
    server.login("erp@solvethenetwork.com", "erpemail@!12")
    server.sendmail(send_from, [send_to], msg.as_string())
    server.close()