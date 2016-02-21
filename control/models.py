from __future__ import unicode_literals
#from django.contrib.auth.models import User
#from django.utils.safestring import mark_safe
from django.db import models
#from django.utils import timezone


class Cargo(models.Model):
    nombre = models.CharField(max_length=100,blank=True,null=False,unique=True)

    class Meta:
        db_table = 'cargo'

    def __unicode__(self):
        return '%s' % (self.nombre)


class Personal(models.Model):
    SEX_CHOICES = (("1", "Masculino"), ("2", "Femenino"))
    cedula = models.CharField(max_length=50, unique=True)
    nombres = models.CharField(max_length=50, blank=True, null=True)
    apellidos = models.CharField(max_length=50, blank=True, null=True)
    telefono1 = models.CharField(max_length=50, blank=True, null=True)
    telefono2 = models.CharField(max_length=50, blank=True, null=True)
    direccion = models.CharField(max_length=500, blank=True, null=True)
    email = models.EmailField(blank=True, null=True)
    sexo = models.CharField(max_length=2, choices=SEX_CHOICES, blank=True, null=True)
    fecha_de_nacimiento = models.DateField(blank=True, null=True)
    cargo = models.ForeignKey(Cargo)

    def get_sex(self):
        if self.sexo == '1':
            return u"Masculino"
        elif self.sexo == '2':
            return u"Femenino"

    class Meta:
        db_table = 'personal'

    def __unicode__(self):
        return '%s (%s %s) %s' % (self.cedula, self.nombres, self.apellidos, self.cargo)


class Inacistencia(models.Model):
    TYPE_CHOICES = (("1", "ASISTENTE PUNTUAL"), ("2", "INASISTENCIA JUSTIFICADA"), ("3", "INASISTENCIA INJUSTIFICADA"), ("4", "ASISTENTE RETARDO"))
    personal = models.ForeignKey(Personal)
    tipo = models.CharField(max_length=2, choices=TYPE_CHOICES, blank=True, null=True)
    fecha = models.DateField()
    estado = models.CharField(max_length=2, choices=TYPE_CHOICES, blank=True, null=True)
    
    def get_type(self):
        if self.tipo == '1':
            return u"ASISTENTE PUNTUAL"
        elif self.tipo == '2':
            return u"INASISTENCIA JUSTIFICADA"
        elif self.tipo == '3':
            return u"INASISTENCIA INJUSTIFICADA"
        elif self.tipo == '4':
            return u"RETARDOS TIEMPO"

    class Meta:
        db_table = 'inacistencia'

    def __unicode__(self):
        return '%s, fecha: %s' % (self.personal, self.fecha)

    