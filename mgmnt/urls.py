from django.conf.urls import url, include
from . import views
from django.contrib.auth.views import LoginView as login_view
from django.contrib.auth.views import LogoutView as logout_view
from global_login_required import login_not_required
from django.conf.urls.static import static
from django.conf import settings

app_name = 'mgmnt'

urlpatterns = [
    url(r'^$', views.home,  name="home"),
    url(r'^login/$', login_not_required(login_view.as_view()), {'template_name': 'mgmnt/login.html'} , name="login_page"),
    url(r'^logout/$', login_not_required(logout_view.as_view()), {'template_name': 'mgmnt/login.html'} , name="logout"),
    url(r'^user/list/$', views.userlist,  name="user-list"),
    url(r'^user/add/$', views.userregistration,  name="user-add"),
    url(r'^user/edit/(?P<id>\d+)/$', views.userregistration,  name="user-edit"),
    url(r'^user/delete/(?P<id>\d+)/$', views.deluser,  name="user-del"),
    url(r'^profile/$', views.userprofile,  name="userprofile"),
    url(r'^profile/edit/$', views.edituserprofile,  name="edituserprofile"),
    url(r'^passchang/$', views.passwordchange,  name="passchang"),
] 
# + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

if settings.DEBUG:
    urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)