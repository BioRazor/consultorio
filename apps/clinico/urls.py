from django.conf.urls import url

from .views import Registro

urlpatterns = [
    url(r'^registro/$', Registro.as_view(), name='registro')
]