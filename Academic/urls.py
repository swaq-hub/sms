from django.conf.urls import url, include
from . import views
from django.contrib.auth.views import LoginView as login_view
from django.contrib.auth.views import LogoutView as logout_view
from global_login_required import login_not_required
from django.conf.urls.static import static
from django.conf import settings

app_name = 'Academic'

urlpatterns = [
                  url(r'^$', views.home,  name="home"),
                  url(r'^period/add$', views.periodaddoredit, name="period-add"),
                  url(r'^period/edit/(?P<id>\d+)/$', views.periodaddoredit, name="period-edit"),
                  url(r'^period/list$', views.period_list, name="period-list"),
                  url(r'^class/add$', views.classaddoredit, name="class-add"),
                  url(r'^class/edit/(?P<id>\d+)/$', views.classaddoredit, name="class-edit"),
                  url(r'^class/list$', views.class_list, name="class-list"),
                  url(r'^subjects/add$', views.subjectsaddoredit, name="subjects-add"),
                  url(r'^subjects/edit/(?P<id>\d+)/$', views.subjectsaddoredit, name="subjects-edit"),
                  url(r'^subjects/list$', views.subjects_list, name="subjects-list"),
              ]
              # + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

if settings.DEBUG:
    urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)