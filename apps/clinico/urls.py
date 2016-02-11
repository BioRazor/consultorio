from django.conf.urls import url

from .views import Registro, Dashboard, LogIn, Logout, SolicitudCita


urlpatterns = [
    url(r'^registro/$', Registro.as_view(), name='registro'),
    url(r'^login/$', LogIn.as_view(), name='login'),
    url(r'^salir/$', Logout, name='logout'),

    url(r'^paciente/$', Dashboard.as_view(), name='dashboard'),
    url(r'^pacientes/cita/$', SolicitudCita.as_view(), name='cita'),


]