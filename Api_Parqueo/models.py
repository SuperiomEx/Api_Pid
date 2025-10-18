from django.db import models
from django.contrib.auth.models import AbstractBaseUser, BaseUserManager
from django.utils import timezone

class UserManager(BaseUserManager):
    def create_user(self, email, nombre, password=None, **extra_fields):
        if not email:
            raise ValueError('El email es obligatorio')
        if not nombre:
            raise ValueError('El nombre es obligatorio')
            
        email = self.normalize_email(email)
        user = self.model(
            email=email,
            nombre=nombre,
            **extra_fields
        )
        user.set_password(password)
        user.save(using=self._db)
        return user

class Usuario(AbstractBaseUser):
    email = models.EmailField(unique=True)
    nombre = models.CharField(max_length=100)
    is_active = models.BooleanField(default=True)
    date_joined = models.DateTimeField(default=timezone.now)
    
    objects = UserManager()
    
    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['nombre']
    
    def __str__(self):
        return self.email

class Parqueo(models.Model):
    nombre = models.CharField(max_length=100)
    direccion = models.CharField(max_length=200)
    tarifa = models.DecimalField(max_digits=5, decimal_places=2)
    
    def __str__(self):
        return self.nombre

class Espacio(models.Model):
    parqueo = models.ForeignKey(Parqueo, on_delete=models.CASCADE)
    numero = models.CharField(max_length=10)
    disponible = models.BooleanField(default=True)
    
    def __str__(self):
        return f"Espacio {self.numero} en {self.parqueo.nombre}"

# Modelo para las reservas
class Reserva(models.Model):
    usuario = models.ForeignKey(Usuario, on_delete=models.CASCADE)
    espacio = models.ForeignKey(Espacio, on_delete=models.CASCADE)
    fecha_inicio = models.DateTimeField()
    fecha_fin = models.DateTimeField()
    pagado = models.BooleanField(default=False)
    
    def __str__(self):
        return f"Reserva de {self.usuario.username}"
