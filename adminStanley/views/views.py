import os
from django.shortcuts import render, redirect
from django.core.handlers.wsgi import WSGIRequest
from django.contrib import messages
from django.http import JsonResponse
from django.contrib.auth.hashers import make_password
from adminStanley.models.models import  RedSocial, Sobremi, stanley, Aptitude
from adminStanley.validator.SobremiValidators import validate_sobremi_data
from adminStanley.Authenticacion.custom_auth import custom_logout, login_required


@login_required
def dashboard(request) :
    context = {"titulo": "Dashboard"}
    return render(request, 'auth/dashboard/index.html',context)

# SOBRE MI

@login_required
def stanleySobremi(request):
    sobremi_obj, created = Sobremi.objects.get_or_create(pk=1)  

    if request.method == 'POST':
        descripcion_inicio = request.POST.get('descripcion_inicio')
        descripcion = request.POST.get('descripcion')

        validation_result = validate_sobremi_data(descripcion_inicio, descripcion)
        if validation_result['valid']:
            sobremi_obj.descripcion_inicio = descripcion_inicio
            sobremi_obj.descripcion = descripcion

            sobremi_obj.save()

            messages.success(request, 'Sobre Mi agregado correctamente.', extra_tags='success')
            return redirect('stanleySobremi')
        else:
            for error_message in validation_result['errors']:
                messages.error(request, error_message)

    context = {"titulo": "Sobre Mi", 'sobremi': sobremi_obj}
    return render(request, 'auth/dashboard/sobreMi/index.html', context)

# FIN SOBRE MI

@login_required
def perfilEditar(request):
    if request.method == 'POST':
        persona = stanley.objects.get(id_persona=request.session['id_persona'])
        ruta_imagen_actual = persona.perfil.path if persona.perfil else None

        imagen_perfil = request.FILES.get('imagen')
        if imagen_perfil:
            if ruta_imagen_actual and os.path.exists(ruta_imagen_actual):
                os.remove(ruta_imagen_actual)

            persona.perfil = imagen_perfil

        persona.nombre_usuario = request.POST.get('nombre_usuario')
        persona.password = request.POST.get('password')
        persona.save()
        messages.success(request, 'Perfil actualizado correctamente.')
        return redirect('perfilEditar') 

    persona = stanley.objects.get(id_persona=request.session['id_persona'])
    context = {"titulo": "Actualizar Perfil", "persona": persona, }
    return render(request, 'auth/dashboard/perfil/editar.html', context)


@login_required
def agregarContacto(request):
    if request.method == 'POST':
        persona = stanley.objects.get(id_persona=request.session['id_persona'])

        redes_sociales = [
            ('facebook', request.POST.get('redes_facebook')),
            ('twitter', request.POST.get('redes_twitter')),
            ('youtube', request.POST.get('redes_youtube')),
            ('instagram', request.POST.get('redes_instagram')),
            ('tiktok', request.POST.get('redes_tiktok')),
            ('github', request.POST.get('redes_github')),
            ('linkedin', request.POST.get('redes_linkedin')),
            ('telegram', request.POST.get('redes_telegram')),
            ('pinterest', request.POST.get('redes_pinterest')),
            ('twitch', request.POST.get('redes_twitch')),
            ('discord', request.POST.get('redes_discord')),
            ('reddit', request.POST.get('redes_reddit')),
            ('email', request.POST.get('redes_email')),
        ]

        for nombre, url in redes_sociales:
            if url is not None and url.strip() != '':
                red_social, created = RedSocial.objects.get_or_create(nombre=nombre)
                red_social.url = url
                red_social.save()
                persona.redes_sociales.add(red_social)
            else:
                red_social = persona.redes_sociales.filter(nombre=nombre).first()
                if red_social:
                    persona.redes_sociales.remove(red_social)
                    red_social.delete()


        persona.save()
        messages.success(request, 'Redes sociales actualizadas correctamente.')
        return redirect('/stanley/contacto')

    persona = stanley.objects.get(id_persona=request.session['id_persona'])
    redes_sociales = RedSocial.objects.all()

    redes_sociales_data = {rs.nombre: rs.url for rs in redes_sociales}

    context = {"titulo": "Agregar Contacto", "redes_sociales": redes_sociales_data}
    return render(request, 'auth/dashboard/perfil/agregar_contacto.html', context)



# APTITUDES
@login_required
def agregarAptitud(request):
    if request.method == 'POST':
        nombre = request.POST.get('nombre')
        if nombre:
            existe_aptitud = Aptitude.objects.filter(nombre=nombre).exists()
            if not existe_aptitud:
                aptitud = Aptitude(nombre=nombre)
                aptitud.save()
                messages.success(request, 'Aptitud agregada correctamente.')
            else:
                messages.error(request, 'Ya existe una aptitud con ese nombre.')
        else:
            messages.error(request, 'El campo de nombre es obligatorio.')
        return redirect('/stanley/aptitud')
    else:
        aptitudes = Aptitude.objects.all()
        context = {"titulo": "Agregar Aptitud", "aptitudes": aptitudes}
        return render(request, 'auth/dashboard/aptitud/agregar.html', context)

@login_required
def eliminar_aptitud(request, aptitud_id):
    try:
        aptitud = Aptitude.objects.get(id_aptitude=aptitud_id)
        aptitud.delete()
        response_data = {'success': True}
    except Aptitude.DoesNotExist:
        response_data = {'success': False, 'error_message': 'La aptitud no existe.'}
    return JsonResponse(response_data)


# FIN APTITUDES

def logout(request):
    custom_logout(request)
    return redirect('/')

    
