from django.conf.urls import url, include
from django.contrib import admin
from django.contrib.auth import views as auth_views
from django.contrib.staticfiles import views
from .views import *
from django.conf import settings
from django.views.static import serve

urlpatterns = [
    url(r'^admin/', admin.site.urls),
    url(r'^', include ('SPP.urls')),
    url(r'^Logout/$', Logout, name="Cerrar sesion"),
    #url(r'^',login_page, name="Inicio de sesion" ),
    url(r'^accounts/login/$', auth_views.login, {'template_name':'login.html'}),
    #url(r'^accounts/logout/$', auth_views.logout, {'template_name':'logout.html'}),
    url(r'^media/(?P<path>.*)$', serve,{'document_root': settings.MEDIA_ROOT, }),
]
