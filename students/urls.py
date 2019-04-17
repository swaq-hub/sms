from django.conf.urls import url, include
from . import views
from django.contrib.auth.views import LoginView as login_view
from django.contrib.auth.views import LogoutView as logout_view
from global_login_required import login_not_required
from django.conf.urls.static import static
from django.conf import settings

app_name = 'students'

urlpatterns = [
    url(r'^$', views.home,  name="home"),
    url(r'^add$', views.studentaddoredit, name="student-add"),
    url(r'^edit/(?P<id>\d+)/$', views.studentaddoredit, name="student-edit"),
    url(r'^list$', views.student_list, name="list"),
    url(r'^admission/add$', views.admissionaddoredit, name="admission-add"),
    url(r'^admission/edit/(?P<id>\d+)/$', views.admissionaddoredit, name="admission-edit"),
    url(r'^admission/list$', views.admissionform_list, name="admission-list"),
    url(r'^attendance$', views.attendanceview, name="attendance"),
    url(r'^profile/(?P<id>\d+)/$', views.showstudentprofile, name="student-profile")
]+ static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)