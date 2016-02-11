from django.conf.urls import url

from .views import Registro, Dashboard, LogIn

urlpatterns = [
    url(r'^registro/$', Registro.as_view(), name='registro'),
    url(r'^pacientes/$', Dashboard.as_view(), name='dashboard'),
    url(r'^login/$', LogIn.as_view(), name='login'),


]