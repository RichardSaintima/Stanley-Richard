from django.shortcuts import render, redirect
from django.core.handlers.wsgi import WSGIRequest
from django.contrib import messages
from proyecto.models import Sobremi, stanley, Certificado, Enlace, Aptitude,Portafolio
from datetime import datetime
from .validators import validate_certificado_data, validate_certificado_data_edit, validate_portafolio_data, validate_portafolio_data_edit, validate_sobremi_data
from proyecto.custom_auth import custom_authenticate, custom_login, custom_logout, login_required


# Create your views here.def index(request):
def index(request):
    context = {
        "titulo": "Inicio"
    }
    return render(request, 'pages/start/index.html', context)



def hobby(request) :
    context ={"titulo": "Hobby"}
    return render(request, 'pages/hobby/blog.html',context)



def portafolio(request) :
    context ={"titulo": "Portafolio"}
    return render(request, 'pages/proyecto/proyecto.html',context)


def sobreMi(request) :
    fecha_nacimiento = datetime(1999, 4, 8)  
    fecha_actual = datetime.now()
    diferencia = fecha_actual - fecha_nacimiento
    edad = diferencia.days // 365
    context = {"titulo": "Sobre Mi",
                "edad": edad}
    return render(request, 'pages/sobre-mi/sobre-mi.html',context)






# ADMIN  ES DECIR YO
def login(request) :
    if request.method == 'POST':
        nombre_usuario = request.POST['nombre_usuario']
        password = request.POST['password']

        try:
            persona = custom_authenticate(nombre_usuario, password)

            if persona is not None:
                custom_login(request, persona)
                if persona:
                    return redirect('/stanley/')
                else:
                    return redirect('/')
            else:
                messages.error(request, 'Credenciales inválidas')
                context = {"titulo": "Iniciar Sesion"}
                return render(request, 'auth/session/login.html', context)

        except stanley.DoesNotExist:
            messages.error(request, 'Credenciales inválidas')
            context = {"titulo": "Iniciar Sesion"}
            return render(request, 'auth/session/login.html', context)

    context ={}
    return render(request, 'auth/session/login.html',context)


@login_required
def dashboard(request) :
    context = {"titulo": "Dashboard"}
    return render(request, 'auth/dashboard/index.html',context)

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
    context = {"titulo": "Agrega Certificado"}
    
    if request.method == 'POST':
        titulo = request.POST.get('nombre')
        nombre_escuela = request.POST.get('nombreEscuela')
        imagen_certificado = request.FILES.get('imagen')
        enlaces = request.POST.getlist('enlaces[]')
        aptitudes = request.POST.getlist('tags')

        validation_result = validate_certificado_data(titulo, nombre_escuela, imagen_certificado, enlaces, aptitudes)

        if validation_result['valid']:
            certificado_obj = Certificado.objects.create(
                titulo=titulo,
                nombre_escuela=nombre_escuela,
                imagen_certificado=imagen_certificado,
            )

            for nombre in enlaces:
                enlace_obj, created = Enlace.objects.get_or_create(nombre=nombre)
                certificado_obj.enlaces.add(enlace_obj)

            if aptitudes:
                for aptitud_nombre in aptitudes:
                    aptitud_existente = Aptitude.objects.filter(nombre=aptitud_nombre).first()
                    if not aptitud_existente:
                        aptitud_obj = Aptitude.objects.create(nombre=aptitud_nombre)
                        aptitud_obj.save()

            certificado_obj.save()

            messages.success(request, 'Certificado agregado correctamente.', extra_tags='success')
            return redirect('/stanley/certificado/')
        else:
            for error_message in validation_result['errors']:
                messages.error(request, error_message)

    return render(request, 'auth/dashboard/certificado/crear.html', context)


@login_required
def editarCertificado(request, pk):
    try:
        certificado = Certificado.objects.get(id_certificado=pk)
    except Certificado.DoesNotExist:
        messages.error(request, 'Error, Certificado no existe')
        return redirect('/stanley/certificado/') 

    if request.method == "POST":
        titulo = request.POST.get('nombre')
        nombre_escuela = request.POST.get('nombreEscuela')
        imagen_certificado = request.FILES.get('imagen')
        enlaces = request.POST.getlist('enlaces[]')
        aptitudes = request.POST.getlist('tags')

        validation_result = validate_certificado_data_edit(titulo, nombre_escuela, enlaces, aptitudes)
        if validation_result['valid']:
            certificado.titulo = titulo
            certificado.nombre_escuela = nombre_escuela

            if imagen_certificado:
                certificado.imagen_certificado = imagen_certificado

            certificado.enlaces.clear()
            for nombre in enlaces:
                enlace_obj, created = Enlace.objects.get_or_create(nombre=nombre)
                certificado.enlaces.add(enlace_obj)

            certificado.aptitudes.clear()
            for aptitud_nombre in aptitudes:
                aptitud_existente = Aptitude.objects.filter(nombre=aptitud_nombre).first()
                if not aptitud_existente:
                    aptitud_nueva = Aptitude.objects.create(nombre=aptitud_nombre)
                    aptitud_nueva.save()
                    certificado.aptitudes.add(aptitud_nueva)
                else:
                    certificado.aptitudes.add(aptitud_existente)

            certificado.save()
            messages.success(request, 'Certificado actualizado correctamente.', extra_tags='success')
            return redirect('/stanley/certificado/')
        else:
            for error_message in validation_result['errors']:
                messages.error(request, error_message)
    context = {
        "titulo": "Actualizar Certificado",
        "certificado": certificado}
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

# PORTAFILO
@login_required
def stanleyPortafolio(request):
    context = {"titulo": "Portafolio"}
    if 'id_persona' in request.session:
        persona = stanley.objects.get(id_persona=request.session['id_persona'])
        portafolios = Portafolio.objects.all()
        context["persona"] = persona
        context["portafolios"] = portafolios
    return render(request, 'auth/dashboard/portafolio/index.html',context)

@login_required
def agregarPortafolio(request):
    context = {"titulo": "Agragar Portafolio"}
    if request.method == 'POST':
        titulo = request.POST.get('nombre')
        descripcion = request.POST.get('descripcion')
        imagen_portafolio = request.FILES.get('imagen')
        rutas_enlaces = request.POST.getlist('enlaces[]')
        aptitudes = request.POST.getlist('tags')

        validation_result = validate_portafolio_data(titulo, imagen_portafolio, descripcion, rutas_enlaces, aptitudes)
        if validation_result['valid']:
            portafolio_obj = Portafolio.objects.create(
                titulo=titulo,
                descripcion=descripcion,
                imagen_portafolio=imagen_portafolio,
            )
            for nombre in rutas_enlaces:
                enlace_obj, created = Enlace.objects.get_or_create(nombre=nombre)
                portafolio_obj.rutas_enlaces.add(enlace_obj)
            if aptitudes:
                for aptitud_nombre in aptitudes:
                    aptitud_existente = Aptitude.objects.filter(nombre=aptitud_nombre).first()
                    if not aptitud_existente:
                        portafolio_obj = Aptitude.objects.create(nombre=aptitud_nombre)
                        portafolio_obj.save()
            portafolio_obj.save()

            messages.success(request, 'Portafolio agregado correctamente.', extra_tags='success')
            return redirect('/stanley/portafolio/')
        else:
            for error_message in validation_result['errors']:
                messages.error(request, error_message)
    return render(request, 'auth/dashboard/portafolio/crear.html', context)



@login_required
def editarPortafolio(request, pk):
    try:
        portafolio = Portafolio.objects.get(id_portafolio=pk)
    except Portafolio.DoesNotExist:
        messages.error(request, 'Error, Certificado no existe')
        return redirect('/stanley/portafolio/') 

    if request.method == "POST":
        titulo = request.POST.get('nombre')
        descripcion = request.POST.get('descripcion')
        imagen_portafolio = request.FILES.get('imagen')
        rutas_enlaces = request.POST.getlist('enlaces[]')
        aptitudes = request.POST.getlist('tags')

        validation_result = validate_portafolio_data_edit(titulo, descripcion, rutas_enlaces, aptitudes)
        if validation_result['valid']:
            portafolio.titulo = titulo
            portafolio.descripcion = descripcion

            if imagen_portafolio:
                portafolio.imagen_portafolio = imagen_portafolio

            portafolio.rutas_enlaces.clear()
            for nombre in rutas_enlaces:
                enlace_obj, created = Enlace.objects.get_or_create(nombre=nombre)
                portafolio.rutas_enlaces.add(enlace_obj)

            portafolio.aptitudes.clear()
            for aptitud_nombre in aptitudes:
                aptitud_existente = Aptitude.objects.filter(nombre=aptitud_nombre).first()
                if not aptitud_existente:
                    aptitud_nueva = Aptitude.objects.create(nombre=aptitud_nombre)
                    aptitud_nueva.save()
                    portafolio.aptitudes.add(aptitud_nueva)
                else:
                    portafolio.aptitudes.add(aptitud_existente)

            portafolio.save()
            messages.success(request, 'Portafolio actualizado correctamente.', extra_tags='success')
            return redirect('/stanley/portafolio/')
        else:
            for error_message in validation_result['errors']:
                messages.error(request, error_message)
    context = {
        "titulo": "Actualizar Portafolio",
        "portafolio": portafolio}
    return render(request, 'auth/dashboard/portafolio/editar.html', context)
            
                

        


@login_required
def eliminarPortafolio(request, pk):
    try:
        portafolio = Portafolio.objects.get(id_portafolio=pk)
        portafolio.delete()
        messages.success(request, 'Portafolio Eliminado correctamente.', extra_tags='success')
        portafolios = Portafolio.objects.all()
        context = {"titulo": "Portafolio", "portafolios": portafolios}
        return render(request, 'auth/dashboard/portafolio/index.html', context)
    except:
        messages.error(request, 'Portafolio no se puede eliminar.')
        portafolios = Portafolio.objects.all()
        context = {"titulo": "Portafolio", "portafolios": portafolios}
        return render(request, 'auth/dashboard/portafolio/index.html', context)

# FIN DEL PROTAFOLIO



# SOBRE MI
@login_required
def stanleySobremi(request):
    if request.method == 'POST':
        descripcion_inicio = request.POST.get('descripcion_inicio')
        descripcion_aptitude = request.POST.get('descripcion_aptitude')
        descripcion = request.POST.get('descripcion')
        aptitudes = request.POST.getlist('tags')

        validation_result = validate_sobremi_data(descripcion_inicio, descripcion_aptitude, descripcion, aptitudes)
        if validation_result['valid']:
            sobremi_obj = Sobremi.objects.create(
                descripcion_inicio=descripcion_inicio,
                descripcion_aptitude=descripcion_aptitude,
                descripcion=descripcion,
            )
            if aptitudes:
                for aptitud_nombre in aptitudes:
                    aptitud_existente = Aptitude.objects.filter(nombre=aptitud_nombre).first()
                    if not aptitud_existente:
                        sobremi_obj = Aptitude.objects.create(nombre=aptitud_nombre)
                        sobremi_obj.save()
            sobremi_obj.save()
            messages.success(request, 'Sobre Mi agregado correctamente.', extra_tags='success')
            return redirect('stanleySobremi')
        else:
            for error_message in validation_result['errors']:
                messages.error(request, error_message)
    sobremi = Sobremi.objects.first() # este Linea es muy Importannte Recuerde 😘😘😘❤️👌❤️
    context = {"titulo": "Sobre Mi", 'sobremi':sobremi}
    return render(request, 'auth/dashboard/sobreMi/index.html',context)     


# FIN SOBRE MI


@login_required
def perfilEditar(request):
    try:
        id_persona = request.session['id_persona']
        persona = stanley.objects.get(id_persona=id_persona)
        
        if request.method == 'POST':
            persona.nombre = request.POST.get('nombre')
            persona.apellido = request.POST.get('apellido')
            persona.nombre_usuario = request.POST.get('nombre_usuario')
            imagen_perfil = request.FILES.get('imagen')
            
            if imagen_perfil:
                persona.perfil = imagen_perfil
            
            persona.linkedin = request.POST.get('linkedin')
            persona.github = request.POST.get('github')
            persona.facebook = request.POST.get('facebook')
            persona.twitter = request.POST.get('twitter')
            persona.instagram = request.POST.get('instagram')
            persona.save()
            messages.success(request, 'Perfil actualizado correctamente.', extra_tags='success')
            return redirect('/stanley/perfil/')
    except stanley.DoesNotExist:
        messages.error(request, 'Error, Persona no existe')
        return redirect('/stanley/perfil/')
    
    context = {"titulo": "Actualiza Perfil", "persona": persona}
    return render(request, 'auth/dashboard/perfil/editar.html', context)


def logout(request):
    custom_logout(request)
    return redirect('/')


def sorry(request: WSGIRequest, exception=None):
    if request.path.startswith("/hobby/"):
        return redirect('hobby')  
    elif request.path.startswith("/sobre-mi/"):
        return redirect('sobre-mi')  
    elif request.path.startswith("/portafolio/"):
        return redirect('portafolio')  
    else:
        return render(request, 'pages/404/404.html', status=404)
 