from django.shortcuts import render, redirect
from django.views.generic import TemplateView

from .forms import LoginForm, RegistroUsuarioForm, RegistroPacienteForm
# Create your views here.
"""
def Registro(request):
	return render(request, 'clinico/registro.html')
"""

class Registro(TemplateView):
	template_name = 'clinico/registro.html'

	def get_context_data(self, **kwargs):
		context = super(Registro, self).get_context_data(**kwargs)
		context['usuarioForm'] = RegistroUsuarioForm()
		context['pacienteForm'] = RegistroPacienteForm()
		return context

	def post(self, request, *args, **kwargs):
		usuario = RegistroUsuarioForm(request.POST)
		
		return redirect('clinico:registro')