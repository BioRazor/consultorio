from django.shortcuts import render, redirect
from django.views.generic import TemplateView
from django.contrib.auth import logout
from braces.views import LoginRequiredMixin

from .models import Usuario, Paciente, Cita, Consulta
from .forms import LoginForm, RegistroUsuarioForm, RegistroPacienteForm
from .functions import Logear
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
		paciente = RegistroPacienteForm(request.POST, request.FILES)
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
			return redirect('clinico:dashboard')
		else:
			context = super(Registro, self).get_context_data(**kwargs)
			context['usuarioForm'] = usuario
			context['pacienteForm'] = paciente
			return render(request, 'clinico/registro.html', context)

class Dashboard(LoginRequiredMixin, TemplateView):
	login_url = 'clinico:login'

	template_name = 'pacientes/dashboard.html'

	def get_context_data(self, **kwargs):
		context = super(Dashboard, self).get_context_data(**kwargs)
		context['paciente'] = Paciente.objects.get(usuario = self.request.user.id)
		context['citas'] = Cita.objects.all().filter(paciente = context['paciente'])
		context['consultas'] = Consulta.objects.all().filter(paciente = context['paciente'])
		return context

class LogIn(TemplateView):
	template_name = 'clinico/login.html'

	def get_context_data(self, **kwargs):
		context = super(LogIn, self).get_context_data(**kwargs)
		context['loginForm'] = LoginForm()
		return context

	def post(self, request, *args, **kwargs):
		login_form = LoginForm(request.POST)
		if login_form.is_valid():
			return Logear(request, login_form.cleaned_data['username'], login_form.cleaned_data['password'])			
		else:
			login_form = LoginForm()
		return render (request, 'administrativo/login.html', {'login_form' : login_form})

def Logout(request):
	logout(request)
	return redirect('/')

class SolicitudCita(TemplateView):
	template_name = 'pacientes/cita.html'

	def get_context_data(self, **kwargs):
		context = super(SolicitudCita, self).get_context_data(**kwargs)
		context['paciente'] = Paciente.objects.get(usuario = self.request.user.id)
		return context