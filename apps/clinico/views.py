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
		paciente = RegistroPacienteForm(request.POST)
		if usuario.is_valid() and paciente.is_valid():
			Usuario.objects.create_user(username= usuario.cleaned_data['username'],
												email = usuario.cleaned_data['email'],
												password = usuario.cleaned_data['password']
												)
			#Se crea un objeto Usuario con el Usuario recien guardado
			usuario = Usuario.objects.get(username = usuario.cleaned_data['username'])
			paciente = paciente.save(commit=False)
			paciente.usuario = usuario
			paciente.save()
			print (paciente)
			print (usuario)
			redirect('clinico:registro')
		else:
			context = super(Registro, self).get_context_data(**kwargs)
			context['usuarioForm'] = usuario
			context['pacienteForm'] = paciente
			return render(request, 'clinico/registro.html', context)