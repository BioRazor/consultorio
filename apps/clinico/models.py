from django.db import models
#imports necesarios para crear un Custom User Manager
from django.contrib.auth.models import AbstractBaseUser, BaseUserManager, PermissionsMixin

#Clase que hereda las funcionalidades y metodo necesario para la creacion de usuarios
class UserManager(BaseUserManager, models.Manager):

	#La siguiente funcion se encarga de crear el usuario en la base de datos, de acuerdo a los parametros recibidos
	def _create_user(self, username, email, password, is_staff,
				is_superuser, **extra_fields):

		#se normaliza y comprueba que se reciba un correro electronico
		email = self.normalize_email(email)
		if not email:
			raise ValueError('El email debe ser obligatorio')

		#Se crea un objeto con los datos recibidos por parametro
		user = self.model(username = username, email=email, is_active=True,
				is_staff = is_staff, is_superuser = is_superuser, **extra_fields)

		#Se realiza el proceso de hash del password o contraseña
		user.set_password(password)

		#Se garda el usuario en la base de datos utilizada actualmente
		user.save( using = self._db)

		#Se retorna el usuario creado
		return user

	def create_user(self, username, email, password=None, **extra_fields):
		return self._create_user(username, email, password, False,
				False, **extra_fields)

	def create_superuser(self, username, email, password=None, **extra_fields):
		return self._create_user(username, email, password, True,
				True, **extra_fields)

#Modelo Usuario, utilizado por el modelo Cliente, el modelo comercio.
#Tambien utilizado como Administrador o superusuario.
class Usuario(AbstractBaseUser, PermissionsMixin):

	username = models.CharField(max_length=100, unique=True)
	email = models.EmailField(unique=True)

	#Se especifica el Manager para el modelo de usuario
	objects = UserManager()

	is_active = models.BooleanField(default = True)
	is_staff = models.BooleanField(default = False)

	#Se especifica el campo a utilizar como Nombre de Usuario
	USERNAME_FIELD = 'username'
	#Se especifican los campos requeridos.
	REQUIRED_FIELDS = ['email']

	#Funcion que retorna el nombre de usuario, como nombre corto del objeto, al realizarse un llamado a este.
	def get_short_name(self):
		return self.username

class Especialidad(models.Model):
	nombre = models.CharField(blank=False, max_length=50)

	def __str__(self):
		return (self.nombre)

	class Meta:
		verbose_name='Especialidad'
		verbose_name_plural='Especialidades'

class Medico(models.Model):
	usuario = models.OneToOneField(Usuario)
	especialidad = models.ManyToManyField(Especialidad)

	nombre = models.CharField(blank=False, max_length=50)
	apellido = models.CharField(blank=False, max_length=50)
	cedula = models.CharField(blank=False, max_length=50)
	foto = models.FileField(upload_to='medicos')

	def __str__(self):
		return (self.nombre)

	class Meta: 
		verbose_name='Medico'
		verbose_name_plural='Medico'

class Paciente(models.Model):
	usuario = models.OneToOneField(Usuario)
	nombre = models.CharField(blank=False, max_length=50)
	apellido = models.CharField(blank=False, max_length=50)
	cedula = models.CharField(blank=False, max_length=50)
	direccion = models.TextField(blank=False)
	foto = models.FileField(upload_to='pacientes')
	choices_prefijo = (
		('0412', '0412'),
		('0416', '0416'),
		('0426', '0426'),
		('0414', '0414'),
		('0424', '0424'),
		)
	prefijo = models.CharField(blank=False, max_length=50, choices=choices_prefijo)
	telefono = models.CharField(blank=False, max_length=50)

	def __str__(self):
		return ('%s %s - %s') %(self.nombre, self.apellido, self.cedula)

	class Meta:
		verbose_name='Paciente'
		verbose_name_plural='Pacientes'

class Cita(models.Model):
	paciente = models.OneToOneField(Paciente)
	medico = models.OneToOneField(Medico)
	fecha = models.DateField()

	def __str__(self):
		return ('%s - %s') %(self.paciente, self.medico)

	class Meta:
		verbose_name='Cita'
		verbose_name_plural='Citas'

class Medicamento(models.Model):
	nombre = models.CharField(blank=False, max_length=50)
	presentacion = models.CharField(blank=False, max_length=50)
	volumen = models.CharField(blank=False, max_length=50)

	descripcion = models.TextField(blank=True)

	def __str__(self):
		return ('%s - %s') %(self.nombre, self.presentacion)

	class Meta:
		verbose_name='Medicamento'
		verbose_name_plural='Medicamentos'

class Consulta(models.Model):
	paciente = models.ForeignKey(Paciente)
	medico = models.ForeignKey(Medico)

	diagnostico = models.TextField(blank=False)
	fecha = models.DateTimeField(auto_now_add=True)

	def __str__(self):
		return ('%s - %s') %(self.paciente, self.medico)

	class Meta:
		verbose_name='Consulta'
		verbose_name_plural='Consultas'
	
class Tratamiento(models.Model):
	consulta = models.ForeignKey(Consulta)
	medicamento = models.ManyToManyField(Medicamento)

	descripcion = models.TextField(blank=False)

	def __str__(self):
		return ('%s - %s') %(self.consulta, self.medicamento)

	class Meta:
		verbose_name='Tratamiento'
		verbose_name_plural='Tratamientos'

class Consultorio(models.Model):
	nombre = models.CharField(blank=False, max_length=50)
	direccion = models.TextField(blank=False)
	mision = models.TextField(blank=False)
	vision = models.TextField(blank=False)
	eslogan = models.CharField(blank=False, max_length=150)
	telefono = models.CharField(blank=False, max_length=50)
	correo = models.EmailField(blank=False)
	foto = models.ImageField(upload_to='home')