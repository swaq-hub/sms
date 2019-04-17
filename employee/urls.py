from django.conf.urls import url, include
from . import views
from django.contrib.auth.views import LoginView as login_view
from django.contrib.auth.views import LogoutView as logout_view
from global_login_required import login_not_required
from django.conf.urls.static import static
from django.conf import settings

app_name = 'employee'

urlpatterns = [
                  url(r'^$', views.home,  name="home"),
                  url(r'^add$', views.employeeaddoredit, name="employee-add"),
                  url(r'^edit/(?P<id>\d+)/$', views.employeeaddoredit, name="employee-edit"),
                  url(r'^list$', views.employee_list, name="list"),
                  url(r'^type_add$', views.employeetypeaddoredit, name="employeetype-add"),
                  url(r'^type_edit/(?P<id>\d+)/$', views.employeetypeaddoredit, name="employeetype-edit"),
                  url(r'^type_list$', views.employeetype_list, name="typelist"),
              ]+ static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

if settings.DEBUG:
	urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)