from django.shortcuts import render
from django.views.generic import TemplateView

from apps.clinico.models import Consultorio


class Home(TemplateView):
	template_name = 'home/index.html'

	def get_context_data(self, **kwargs):
		context = super(Home, self).get_context_data(**kwargs)
		context['consultorio'] = Consultorio.objects.get()
		return context	
