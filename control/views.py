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

@csrf_protect
def get_cargos(request):
    cargos = Cargo.objects.all()
    dicc = {}
    lista = []
    for x in cargos:
        dicc = {
            "id" : x.id,
            "cargo" : x.nombre,
        }
        lista.append(dicc)
    result = json.dumps(lista, ensure_ascii=False)
    return HttpResponse(result, content_type='application/json; charset=utf-8')


@csrf_protect
def delete_cargo(request):
    message =''
    cargos = Cargo.objects.get(id=request.POST['id'])
    cargos.delete()
    message ='Borrado'
    result = json.dumps(message, ensure_ascii=False)
    return HttpResponse(result, content_type='application/json; charset=utf-8')


@csrf_protect
def delete_person(request):
    message =''
    personal = Personal.objects.get(id=request.POST['id'])
    personal.delete()
    message ='Borrado'
    result = json.dumps(message, ensure_ascii=False)
    return HttpResponse(result, content_type='application/json; charset=utf-8')


@csrf_protect
def crear_cargos(request):
    mensaje = ''
    if request.method == "POST":
        if not Cargo.objects.filter(nombre=request.POST['cargo']).exists():
            cargo = Cargo(
                nombre=request.POST['cargo']
            )
            cargo.save()
            mensaje = 'Guardado'
        else:
            mensaje = 'Cargo ya Existe'
    result = json.dumps(mensaje, ensure_ascii=False)
    return HttpResponse(result, content_type='application/json; charset=utf-8')


def edit_cargos(request):
    message = ''
    cargo = Cargoargo.objects.filter(id=request.POST['id']).update(
            nombre=request.POST['cargo']
        )
    message = "Guardado"
    result = json.dumps(mensaje, ensure_ascii=False)
    return HttpResponse(result, content_type='application/json; charset=utf-8')

@csrf_protect
def crear_personal(request):
    mensaje = ''
    if request.method == "POST":
        if not Personal.objects.filter(cedula=request.POST['cedula']).exists():
            cargo = Cargo.objects.get(nombre=request.POST['cargo'])
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
                cargo = cargo,
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
            "cargo": str(x.cargo),
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
        inacistencia = Inacistencia.objects.filter(id=request.POST['id_personal']).update(
            personal_id=request.POST['id_personal'],
            tipo=request.POST['tipo'],
        )
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
        )
        if request.POST.has_key('year'):
            inacistencia =    inacistencia.filter(fecha__year=request.POST["year"])
        if request.POST.has_key('cargo'):
            inacistencia =    inacistencia.filter(cargo=request.POST["cargo"])
        if request.POST.has_key('month'):
            inacistencia =    inacistencia.filter(fecha__month=request.POST["month"])
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
        personal_id=request.GET["id_personal"],
    )
    for y in inacistencia:
        dicc = {}
        dicc = {
            "id": y.id,
            "tipo": y.get_type(),
            "fecha": str(y.fecha.strftime('%Y-%m-%d'))
        }
        lista.append(dicc)
    result = json.dumps(lista, ensure_ascii=False)
    return HttpResponse(result, content_type='application/json; charset=utf-8')

class index(TemplateView):
    template_name = 'index.html'
    def get(self, request, *args, **kwargs):
        cargos = Cargo.objects.filter()
        year = Inacistencia.objects.all()
        lista =[]
        for x in year:
            if not x.fecha.year in lista:
                lista.append(x.fecha.year)

        return render_to_response(self.template_name, locals(), context_instance=RequestContext(request))