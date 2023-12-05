from django.shortcuts import render, redirect
from django.contrib import messages
from django.db import transaction
from adminStanley.models.models import  stanley, Certificado, Aptitude
from adminStanley.validator.CertificadoValidacion import validate_certificado_data, validate_certificado_data_edit
from adminStanley.Authenticacion.custom_auth import login_required
# CERTIFICADO
@login_required
def stanleyCertificado(request):
    context = {"titulo": "Certificado"}  
    if 'id_persona' in request.session:
        persona = stanley.objects.get(id_persona=request.session['id_persona'])
        certificados = Certificado.objects.all()
        context["persona"] = persona
        context["certificados"] = certificados
    return render(request, 'auth/dashboard/certificado/index.html', context)

@login_required
def agregarCertificado(request):
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
            certificado_obj = Certificado.objects.create(
                titulo=titulo,
                nombre_escuela=nombre_escuela,
                imagen_certificado=imagen_certificado,
                enlaces_web=enlaces_web,
            )

            for aptitud_id in aptitudes:
                if not aptitud_id:
                    messages.error(request, 'Error: Aptitud inválida.')
                    return redirect('agregarCertificado')

                try:
                    aptitud = Aptitude.objects.get(id_aptitude=aptitud_id)
                    certificado_obj.aptitudes.add(aptitud)
                except (Aptitude.DoesNotExist, ValueError):
                    messages.error(request, f'Aptitud con ID {aptitud_id} no encontrada.')
                    return redirect('agregarCertificado')
                
            messages.success(request, 'Certificado agregado correctamente.', extra_tags='success')
            return redirect('/stanley/certificado/')
        else:
            for error_message in validation_result['errors']:
                messages.error(request, error_message)

    aptitudes = Aptitude.objects.all()
    context = {
        "titulo": "Agrega Certificado",
        "aptitudes": aptitudes,
    }
    return render(request, 'auth/dashboard/certificado/crear.html', context)


@transaction.atomic
@login_required
def editarCertificado(request, pk):
    try:
        certificado = Certificado.objects.get(id_certificado=pk)
    except Certificado.DoesNotExist:
        messages.error(request, 'Error, Certificado no existe')
        return redirect('/stanley/certificado/')

    aptitudes = Aptitude.objects.all()

    if request.method == "POST":
        titulo = request.POST.get('nombre')
        nombre_escuela = request.POST.get('nombreEscuela')
        imagen_certificado = request.FILES.get('imagen')
        enlaces_web = request.POST.get('enlaces_web')
        aptitudes_ids = request.POST.getlist('aptitudes')

        validation_result = validate_certificado_data_edit(titulo, nombre_escuela, enlaces_web, aptitudes_ids)

        if validation_result['valid']:
            certificado.titulo = titulo  if titulo is not None else certificado.titulo
            certificado.nombre_escuela = nombre_escuela if nombre_escuela is not None else certificado.nombre_esc
            certificado.imagen_certificado = imagen_certificado if imagen_certificado is not None else certificado.imagen_certificado
            certificado.enlaces_web = enlaces_web if enlaces_web is not None else certificado.enlaces_web
            certificado.aptitudes.set(aptitudes_ids)

            certificado.save()
            messages.success(request, 'Certificado actualizado correctamente.', extra_tags='success')
            return redirect('/stanley/certificado/')
        else:
            for error_message in validation_result['errors']:
                messages.error(request, error_message)

    context = {
        "titulo": "Actualizar Certificado",
        "certificado": certificado,
        "aptitudes": aptitudes,
    }
    return render(request, 'auth/dashboard/certificado/editar.html', context)


@login_required
def eliminarCertificado(request,pk):
    try:
        certificado = Certificado.objects.get(id_certificado=pk)
        certificado.delete()
        messages.success(request, 'Certificado Eliminado correctamente.', extra_tags='success')
        certificados = Certificado.objects.all()
        context = {"titulo": "Certificado",
                    "certificados": certificados}
        return render(request, 'auth/dashboard/certificado/index.html', context)
    except:
        messages.error(request, 'Certificado no se puede eliminar.')
        certificados = Certificado.objects.all()
        context = {"titulo": "Certificado",
                    "certificados": certificados}
        return render(request, 'auth/dashboard/certificado/index.html', context)

# FIN DEL CERTIFICADO