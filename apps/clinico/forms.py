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

    def clean_password(self):
      password1 = self.cleaned_data.get('password')
      password2 = self.cleaned_data.get('passwordCheck')

      if not password2:
          raise forms.ValidationError("Debes verificar tu contraseña.")
      if password1 != password2:
          raise forms.ValidationError("Las contraseñas no coinciden")
      return password2

class RegistroPacienteForm(forms.ModelForm):
  class Meta:
    model = Paciente
    exclude= ('usuario',)
    widgets= {
      'nombre' : forms.TextInput(),
      'apellido' : forms.TextInput(),
      'cedula' : forms.TextInput(),
      'direccion' : forms.Textarea(),
      'foto' : forms.FileInput(attrs={'class' : ''}),
      'prefijo' : forms.Select(),
      'telefono' : forms.TextInput(),


    }
