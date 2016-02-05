from django import forms

from .models import Usuario, Paciente

class LoginForm(forms.Form):

  username = forms.CharField(max_length=30, 
        widget= forms.TextInput(attrs={
          'class' : '',
          'placeholder' : 'Ingresa tu Nombre de Usuario'
          }))
  password = forms.CharField(max_length=30, 
        widget= forms.TextInput(attrs={
          'type' : 'password',
          'class' : '',
          'placeholder' : 'Ingresa tu Contraseña'
          }))

class RegistroUsuarioForm(forms.ModelForm):
  passwordCheck = forms.CharField(max_length=30, widget=forms.TextInput(
                                attrs={'class' : '',
                                    'placeholder': 'Escribe de nuevo la contraseña',
                                    'required' : 'True',
                                    'type' : 'password'
                                }))
  class Meta:
    model = Usuario
    fields = ('username', 'email', 'password')
    widgets = {
      'username' : forms.TextInput(attrs = 
        {
        'class' : '', 
        }),
      'email' : forms.TextInput(attrs = 
        {
        'type' : 'email',
        'class' : '',
        }),
      'password' : forms.TextInput(attrs = 
        {
        'type' : 'password',
        'class' : '',
        'required' : 'True'
        })
    }

class RegistroPacienteForm(forms.ModelForm):
  class Meta:
    model = Paciente
    exclude= ('usuario',)
    widgets= {
      'nombre' : forms.TextInput(attrs = { 'class' : ''}),
      'apellido' : forms.TextInput(attrs = { 'class' : ''}),
      'cedula' : forms.TextInput(attrs = { 'class' : ''}),
      'direccion' : forms.Textarea(attrs = { 'class' : ''}),
      'foto' : forms.FileInput(attrs = { 'class' : ''}),
      'prefijo' : forms.TextInput(attrs = { 'class' : ''}),
      'telefono' : forms.TextInput(attrs = { 'class' : ''}),


    }
