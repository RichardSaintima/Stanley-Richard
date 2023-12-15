import os
from django.shortcuts import render, redirect
from django.contrib import messages
from django.db import transaction
from adminStanley.models.models import Stanley, Certificado, Aptitude
from adminStanley.validator.CertificadoValidacion import validate_certificado_data, validate_certificado_data_edit
from adminStanley.Authenticacion.custom_auth import login_required

# CERTIFICADO

TEMPLATE_INDEX = 'auth/dashboard/certificado/index.html'
TEMPLATE_CREAR = 'auth/dashboard/certificado/crear.html'
TEMPLATE_EDITAR = 'auth/dashboard/certificado/editar.html'

@login_required
def stanley_certificado(request):
    context = {"titulo": "Certificado"}  
    if 'id_persona' in request.session:
        persona = Stanley.objects.get(id_persona=request.session['id_persona'])
        certificados = Certificado.objects.all()
        context["persona"] = persona
        context["certificados"] = certificados
    return render(request, TEMPLATE_INDEX, context)

@login_required
def agregar_certificado(request):
    if request.method == 'POST':
        titulo = request.POST.get('nombre')
        nombre_escuela = request.POST.get('nombreEscuela')
        imagen_certificado = request.FILES.get('imagen')
        enlaces_web = request.POST.get('enlaces_web')
        if 'aptitudes' in request.POST:
            aptitudes = request.POST.getlist('aptitudes')
        else:
            aptitudes = []  

        validation_result = validate_certificado_data(titulo, nombre_escuela, imagen_certificado, enlaces_web, aptitudes)

        if validation_result['valid']:
            certificado_obj = create_certificado(titulo, nombre_escuela, imagen_certificado, enlaces_web)
            add_aptitudes(certificado_obj, aptitudes, request) 

            messages.success(request, 'Certificado agregado correctamente.', extra_tags='success')
            return redirect('stanley_certificado')
        else:
            for error_message in validation_result['errors']:
                messages.error(request, error_message)

    aptitudes = Aptitude.objects.all()
    context = {
        "titulo": "Agrega Certificado",
        "aptitudes": aptitudes,
    }
    return render(request, TEMPLATE_CREAR, context)

def create_certificado(titulo, nombre_escuela, imagen_certificado, enlaces_web):
    return Certificado.objects.create(
        titulo=titulo,
        nombre_escuela=nombre_escuela,
        imagen_certificado=imagen_certificado,
        enlaces_web=enlaces_web,
    )

def add_aptitudes(certificado_obj, aptitudes, request):
    for aptitud_id in aptitudes:
        if not aptitud_id:
            messages.error(request, 'Error: Aptitud inválida.')
            return redirect('agregar_certificado')

        try:
            aptitud = Aptitude.objects.get(id_aptitude=aptitud_id)
            certificado_obj.aptitudes.add(aptitud)
        except (Aptitude.DoesNotExist, ValueError):
            messages.error(request, f'Aptitud con ID {aptitud_id} no encontrada.')
            return redirect('agregar_certificado')


# EDITAR
@transaction.atomic
@login_required
def editar_certificado(request, pk):
    try:
        certificado = Certificado.objects.get(id_certificado=pk)
    except Certificado.DoesNotExist:
        messages.error(request, 'Error, Certificado no existe')
        return redirect('stanley_certificado')

    aptitudes = Aptitude.objects.all()

    if request.method == "POST":
        titulo = request.POST.get('nombre')
        nombre_escuela = request.POST.get('nombreEscuela')
        imagen_certificado = request.FILES.get('imagen')
        enlaces_web = request.POST.get('enlaces_web')
        aptitudes_ids = request.POST.getlist('aptitudes')

        validation_result = validate_certificado_data_edit(titulo, nombre_escuela, enlaces_web, aptitudes_ids)

        if validation_result['valid']:
            ruta_imagen_actual = certificado.imagen_certificado.path if certificado.imagen_certificado else None
            if ruta_imagen_actual and imagen_certificado:
                os.remove(ruta_imagen_actual)

            update_certificado(certificado, titulo, nombre_escuela, imagen_certificado, enlaces_web, aptitudes_ids)

            messages.success(request, 'Certificado actualizado correctamente.', extra_tags='success')
            return redirect('stanley_certificado')
        else:
            for error_message in validation_result['errors']:
                messages.error(request, error_message)

    context = {
        "titulo": "Actualizar Certificado",
        "certificado": certificado,
        "aptitudes": aptitudes,
    }
    return render(request, TEMPLATE_EDITAR, context)


def update_certificado(certificado, titulo, nombre_escuela, imagen_certificado, enlaces_web, aptitudes_ids):
    certificado.titulo = titulo if titulo is not None else certificado.titulo
    certificado.nombre_escuela = nombre_escuela if nombre_escuela is not None else certificado.nombre_escuela
    certificado.imagen_certificado = imagen_certificado if imagen_certificado is not None else certificado.imagen_certificado
    certificado.enlaces_web = enlaces_web if enlaces_web is not None else certificado.enlaces_web
    certificado.aptitudes.set(aptitudes_ids)

    certificado.save()


# ELIMINAR
@login_required
def eliminar_certificado(request, pk):
    try:
        certificado = Certificado.objects.get(id_certificado=pk)
        ruta_imagen_actual = certificado.imagen_certificado.path

        certificado.delete()

        if os.path.exists(ruta_imagen_actual):
            os.remove(ruta_imagen_actual)

        messages.success(request, 'Certificado eliminado correctamente.', extra_tags='success')
        return redirect('stanley_certificado')

    except Certificado.DoesNotExist:
        messages.error(request, 'Certificado no encontrado.')
    except FileNotFoundError:
        messages.warning(request, 'El archivo de imagen no se encontró.')

    certificados = Certificado.objects.all()
    context = {
        "titulo": "Certificado",
        "certificados": certificados,
    }
    return render(request, TEMPLATE_INDEX, context)

# FIN DEL CERTIFICADO
