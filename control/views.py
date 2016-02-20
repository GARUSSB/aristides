# -*- encoding: utf-8 -*-
from django.views.generic import TemplateView
from django.contrib.auth.models import User, Group, Permission
from django.contrib.auth.decorators import login_required, permission_required
from django.http import HttpResponseNotFound, HttpResponseRedirect
from django.shortcuts import render_to_response, HttpResponse, render, get_object_or_404
from django.template import RequestContext
from .models import * 
import json
from django.conf import settings as _settings
from django.contrib.auth import login, logout, authenticate
from django.core.mail import get_connection, send_mail, BadHeaderError
from django.utils import timezone
from django.views.decorators.csrf import csrf_protect

def set_cargos(request):
    mensaje = ''
    if not Cargos.objects.filter(nombre=request.POST['nombre']).exists():
        cargos=  Cargos(
                nombre=request.POST['nombre'],
            )
        cargos.save()
        mensaje= 'Guardado'
    else:
        mensaje= 'Cargo ya existe'
def get_cargos(request):
    cargos = Cargo.objects.all()
    dicc = {}
    lista = []
    for x in personal:
        dicc = {
         cargo : x.nombre
        }
        lista.append(dicc)
    result = json.dumps(lista, ensure_ascii=False)
    return HttpResponse(result, content_type='application/json; charset=utf-8')
@csrf_protect
def crear_personal(request):
    mensaje = ''
    if request.method == "POST":
        if not Personal.objects.filter(cedula=request.POST['cedula']).exists():
            personal = Personal(
                cedula=request.POST['cedula'],
                nombres=request.POST['nombre'],
                apellidos=request.POST['apellido'],
                telefono1=request.POST['telefono1'],
                telefono2=request.POST['telefono2'],
                direccion=request.POST['direccion'],
                email=request.POST['email'],
                sexo=request.POST['sexo'],
                fecha_de_nacimiento=request.POST['fecha_de_nacimiento'],
                cargo = request.POST['cargo'],
            )
            personal.save()
            mensaje = 'Guardado'
        else:
            mensaje = 'Alumno Ya Existe'
    result = json.dumps(mensaje, ensure_ascii=False)
    return HttpResponse(result, content_type='application/json; charset=utf-8')


def editar_personal(request):
    mensaje = ''
    personal = Personal.objects.filter(id=request.POST['id']).update(
        cedula=request.POST['cedula'],
        nombres=request.POST['nombres'],
        apellidos=request.POST['apellidos'],
        telefono1=request.POST['telefono1'],
        telefono2=request.POST['telefono2'],
        direccion=request.POST['direccion'],
        email=request.POST['email'],
        sexo=request.POST['sexo'],
        fecha_de_nacimiento=request.POST['fecha_de_nacimiento'],
    )
    mensaje = 'Guardado'
    result = json.dumps(mensaje, ensure_ascii=False)
    return HttpResponse(result, content_type='application/json; charset=utf-8')


def get_all_personal(request):
    personal = Personal.objects.all()
    dicc = {}
    lista = []
    for x in personal:
        dicc = {
            "id": x.id,
            "cedula": x.cedula,
            "nombres": x.nombres,
            "apellidos": x.apellidos,
            "telefono1": x.telefono1,
            "telefono2": x.telefono2,
            "direccion": x.direccion,
            "email": x.email,
            "sexo": x.sexo,
            "fecha_de_nacimiento": str(x.fecha_de_nacimiento),
        }
        lista.append(dicc)
        dicc = {}
    result = json.dumps(lista, ensure_ascii=False)
    return HttpResponse(result, content_type='application/json; charset=utf-8')

def get_personal(request):
    personal = Personal.objects.get(id=request.POST['id'])
    dicc = {}
    dicc = {
        "id": personal.id,
        "cedula": personal.cedula,
        "nombres": personal.nombres,
        "apellidos": personal.apellidos,
        "telefono1": personal.telefono1,
        "telefono2": personal.telefono2,
        "direccion": personal.direccion,
        "email": personal.email,
        "sexo": personal.sexo,
        "fecha_de_nacimiento": str(personal.fecha_de_nacimiento),
    }
    result = json.dumps(dicc, ensure_ascii=False)
    return HttpResponse(result, content_type='application/json; charset=utf-8')


def crear_inacistencia(request):
    mensaje = ''
    now = timezone.now().date()
    if not Inacistencia.objects.filter(personal=request.POST['id_personal'], fecha=now).exists():
        inacistencia = Inacistencia(
            personal_id=request.POST['id_personal'],
            tipo=request.POST['tipo'],
            fecha=now,
        )
        inacistencia.save()
        mensaje = 'Guardado'
    else:
        mensaje = 'ya registro la asistencia de hoy'
    result = json.dumps(mensaje, ensure_ascii=False)
    return HttpResponse(result, content_type='application/json; charset=utf-8')


def editar_inacistencia(request):
    mensaje = ''
    inacistencia = Inacistencia.objects.filter(id=request.POST['id']).update(
        personal_id=request.POST['id_personal'],
        tipo=request.POST['tipo'],
        fecha=request.POST['fecha'],
    )
    mensaje = 'Guardado'
    result = json.dumps(mensaje, ensure_ascii=False)
    return HttpResponse(result, content_type='application/json; charset=utf-8')


def get_all_inacistencia(request):
    dicc = {}
    lista = []
    lista2 = []
    personal = Personal.objects.all()
    for x in personal:
        inacistencia = Inacistencia.objects.filter(
            personal=x,
            fecha__year=request.POST["year"],
            fecha__month=request.POST["month"],
        )
        for y in inacistencia:
            dicc = {}
            dicc = {
                "id": y.id,
                "tipo": y.tipo,
                "fecha": y.fecha.strftime('%Y-%m-%d')
            }
            lista.append(dicc)
        dicc = {}
        dicc = {
            "id": x.id,
            "cedula": x.cedula,
            "nombres": x.nombres,
            "apellidos": x.apellidos,
            "telefono1": x.telefono1,
            "telefono2": x.telefono2,
            "direccion": x.direccion,
            "email": x.email,
            "sexo": x.sexo,
            "fecha_de_nacimiento": str(x.fecha_de_nacimiento),
            "asistencia": lista
        }
        lista2.append(dicc)
        lista = []
        dicc = {}
    result = json.dumps(lista2, ensure_ascii=False)
    return HttpResponse(result, content_type='application/json; charset=utf-8')


def get_personal_inacistencia(request):
    dicc = {}
    lista = []
    inacistencia = Inacistencia.objects.filter(
        personal_id=request.POST["id_personal"],
        fecha__year=request.POST["year"],
        fecha__month=request.POST["month"],
        fecha__day=request.POST["day"],
    )
    for y in inacistencia:
        dicc = {}
        dicc = {
            "id": y.id,
            "tipo": y.tipo,
            "fecha": str(y.fecha.strftime('%Y-%m-%d'))
        }
        lista.append(dicc)
    dicc = {}
    dicc = {
        "id": x.id,
        "cedula": x.cedula,
        "nombres": x.nombres,
        "apellidos": x.apellidos,
        "telefono1": x.telefono1,
        "telefono2": x.telefono2,
        "direccion": x.direccion,
        "email": x.email,
        "sexo": x.sexo,
        "fecha_de_nacimiento": str(x.fecha_de_nacimiento),
        "asistencia": lista
    }
    result = json.dumps(dicc, ensure_ascii=False)
    return HttpResponse(result, content_type='application/json; charset=utf-8')
class index(TemplateView):
    template_name = 'index.html'
    def get(self, request, *args, **kwargs):
        cargos = Cargo.objects.filter()
        return render_to_response(self.template_name, locals(), context_instance=RequestContext(request))
