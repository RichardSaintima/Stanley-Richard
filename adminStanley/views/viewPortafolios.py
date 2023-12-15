from django.shortcuts import render, redirect
from django.contrib import messages
from django.db import transaction
import os
from adminStanley.models.models import Stanley, Portafolio, Aptitude, Estado
from adminStanley.Authenticacion.custom_auth import login_required
from adminStanley.validator.PortafolioValidacion import validate_portafolio_data, validate_portafolio_data_edit
from django.http import request

TEMPLATE_INDEX = 'auth/dashboard/portafolio/index.html'
TEMPLATE_CREAR = 'auth/dashboard/portafolio/crear.html'
TEMPLATE_EDITAR = 'auth/dashboard/portafolio/editar.html'
# PORTAFOLIO
@login_required
def stanley_portafolio(request):
    context = {"titulo": "Portafolio"}
    if 'id_persona' in request.session:
        persona = Stanley.objects.get(id_persona=request.session['id_persona'])
        portafolios = Portafolio.objects.all()
        context["persona"] = persona
        context["portafolios"] = portafolios
    return render(request, TEMPLATE_INDEX, context)

@login_required
def agregar_portafolio(request):
    if request.method == 'POST':
        titulo = request.POST.get('nombre')
        imagen_portafolio = request.FILES.get('imagen')
        descripcion = request.POST.get('descripcion')
        enlaces_web = request.POST.get('enlaces_web')
        enlaces_github = request.POST.get('enlaces_github')
        id_estado = request.POST.get('id_estado')
        if 'aptitudes' in request.POST:
            aptitudes = request.POST.getlist('aptitudes')
        else:
            aptitudes = []

        validation_result = validate_portafolio_data(titulo,imagen_portafolio, descripcion, enlaces_web, enlaces_github,id_estado, aptitudes)

        if validation_result['valid']:
            portafolio_obj = create_portafolio(titulo, imagen_portafolio, descripcion, enlaces_web, enlaces_github,id_estado)
            add_aptitudes(portafolio_obj, aptitudes, request)

            messages.success(request, 'Portafolio agregado correctamente.', extra_tags='success')
            return redirect('stanley_portafolio')
        else:
            for error_message in validation_result['errors']:
                messages.error(request, error_message)

    aptitudes = Aptitude.objects.all()
    estados = Estado.objects.all()
    context = {
        "titulo": "Agregar Portafolio",
        "aptitudes": aptitudes,
        "estados": estados,
    }
    return render(request, TEMPLATE_CREAR, context)

def create_portafolio(titulo, imagen_portafolio, descripcion, enlaces_web, enlaces_github, id_estado):
    try:
        estado = Estado.objects.get(id_estado=id_estado)
    except Estado.DoesNotExist:
        # Manejar el caso donde el Estado no existe
        messages.error(request, f'Estado con ID {id_estado} no encontrado.')
        return None

    return Portafolio.objects.create(
        titulo=titulo,
        imagen_portafolio=imagen_portafolio,
        descripcion=descripcion,
        enlaces_web=enlaces_web,
        enlaces_github=enlaces_github,
        id_estado=estado
    )


def add_aptitudes(portafolio_obj, aptitudes, request):
    for aptitud_id in aptitudes:
        if not aptitud_id:
            messages.error(request, 'Error: Aptitud inválida.')
            return redirect('agregar_portafolio')

        try:
            aptitud = Aptitude.objects.get(id_aptitude=aptitud_id)
            portafolio_obj.aptitudes.add(aptitud)
        except (Aptitude.DoesNotExist, ValueError):
            messages.error(request, f'Aptitud con ID {aptitud_id} no encontrada.')
            return redirect('agregar_portafolio')




# EDITAR
@transaction.atomic
@login_required
def editar_portafolio(request, pk):
    try:
        portafolio = Portafolio.objects.get(id_portafolio=pk)
    except Portafolio.DoesNotExist:
        messages.error(request, 'Error, Portafolio no existe')
        return redirect('stanley_portafolio')

    aptitudes = Aptitude.objects.all()
    estados = Estado.objects.all()

    if request.method == "POST":
        return handle_post_request(request, portafolio, aptitudes, estados)

    context = {
        "titulo": "Editar Portafolio",
        "portafolio": portafolio,
        "aptitudes": aptitudes,
        "estados": estados,
    }
    return render(request, TEMPLATE_EDITAR, context)

def handle_post_request(request, portafolio, aptitudes, estados):
    titulo = request.POST.get('nombre')
    descripcion = request.POST.get('descripcion')
    imagen_portafolio = request.FILES.get('imagen')
    enlaces_web = request.POST.get('enlaces_web')
    enlaces_github = request.POST.get('enlaces_github')
    aptitudes_ids = request.POST.getlist('aptitudes')
    id_estado = request.POST.get('id_estado')

    validation_result = validate_portafolio_data_edit(titulo, descripcion, enlaces_web, enlaces_github, aptitudes_ids)

    if validation_result['valid']:
        if id_estado is not None and id_estado.isdigit():
            estado = Estado.objects.get(id_estado=int(id_estado))

            ruta_imagen_actual = portafolio.imagen_portafolio.path if portafolio.imagen_portafolio else None
            if ruta_imagen_actual and imagen_portafolio:
                os.remove(ruta_imagen_actual)

            update_portafolio(
                portafolio,
                titulo,
                descripcion,
                imagen_portafolio,
                enlaces_web,
                enlaces_github,
                aptitudes_ids,
                estado
            )

            messages.success(request, 'Portafolio actualizado correctamente.', extra_tags='success')
            return redirect('stanley_portafolio')
        else:
            messages.error(request, 'Error: Estado inválido.')
    else:
        for error_message in validation_result['errors']:
            messages.error(request, error_message)

    context = {
        "titulo": "Editar Portafolio",
        "portafolio": portafolio,
        "aptitudes": aptitudes,
        "estados": estados,
    }
    return render(request, TEMPLATE_EDITAR, context)


def update_portafolio(portafolio, titulo, descripcion, imagen_portafolio, enlaces_web, enlaces_github, aptitudes_ids, estado):
    portafolio.imagen_portafolio = imagen_portafolio if imagen_portafolio is not None else portafolio.imagen_portafolio
    portafolio.titulo = titulo if titulo is not None else portafolio.titulo
    portafolio.descripcion = descripcion if descripcion is not None else portafolio.descripcion
    portafolio.enlaces_web = enlaces_web if enlaces_web is not None else portafolio.enlaces_web
    portafolio.enlaces_github = enlaces_github if enlaces_github is not None else portafolio.enlaces_github
    portafolio.id_estado = estado if estado is not None else portafolio.id_estado
    portafolio.aptitudes.set(aptitudes_ids)

    portafolio.save()



@login_required
def eliminar_portafolio(request, pk):
    try:
        portafolio = Portafolio.objects.get(id_portafolio=pk)
        ruta_imagen_actual = portafolio.imagen_portafolio.path
        portafolio.delete()

        if os.path.exists(ruta_imagen_actual):
            os.remove(ruta_imagen_actual)

        messages.success(request, 'Portafolio Eliminado correctamente.', extra_tags='success')
        portafolios = Portafolio.objects.all()
        context = {"titulo": "Portafolio", "portafolios": portafolios}
        return render(request, TEMPLATE_INDEX, context)
    except:
        messages.error(request, 'Portafolio no se puede eliminar.')
        portafolios = Portafolio.objects.all()
        context = {"titulo": "Portafolio", "portafolios": portafolios}
        return render(request, TEMPLATE_INDEX, context)
        raise

# FIN DEL PROTAFOLIO
