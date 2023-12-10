from django.shortcuts import render, redirect
from django.contrib import messages
from adminStanley.models.models import Estado, Sobremi, stanley, Certificado, Aptitude, Portafolio
from datetime import datetime
from django.http import HttpResponse
from django.core.mail import EmailMessage
from django.template.loader import render_to_string
from django.conf import settings
from adminStanley.Authenticacion.custom_auth import custom_authenticate, custom_login, custom_logout
from proyecto.Authenticacion.custom_auth import check_session


def obtener_datos_generales():
    persona = stanley.objects.first()
    redes_sociales = persona.redes_sociales.all()
    return persona, redes_sociales

@check_session
def inicio(request, session):
    persona, redes_sociales = obtener_datos_generales()
    sobremi = Sobremi.objects.first()
    context = {"titulo": "Inicio", "persona": persona, "session": session, "sobremi": sobremi,"redes_sociales": redes_sociales,}
    return render(request, 'pages/start/inicio.html', context)

@check_session
def index(request, session):
    persona, redes_sociales = obtener_datos_generales()
    sobremi = Sobremi.objects.first()
    certificados = Certificado.objects.all()
    aptitudes = Aptitude.objects.all()

    fecha_nacimiento = datetime(1999, 4, 8)
    fecha_actual = datetime.now()
    diferencia = fecha_actual - fecha_nacimiento
    edad = diferencia.days // 365

    portafolios_completados = Portafolio.objects.filter(id_estado__nombre="Completado")
    portafolios_pendientes = Portafolio.objects.filter(id_estado__nombre="Pendiente")

    context = {
        "persona": persona,
        "session": session,
        "redes_sociales": redes_sociales,
        "sobremi": sobremi,
        "certificados": certificados,
        "aptitudes": aptitudes,
        "edad": edad,
        "portafolios_completados": portafolios_completados,
        "portafolios_pendientes": portafolios_pendientes,
    }
    return render(request, 'pages/index.html', context)

@check_session
def hobby(request, session):
    persona, redes_sociales = obtener_datos_generales()
    context = {"titulo": "Mi Hobby", "session": session, "persona": persona, "redes_sociales": redes_sociales}
    return render(request, 'pages/hobby/blog.html', context)

@check_session
def portafolio(request, session):
    persona, redes_sociales = obtener_datos_generales()
    estados = Estado.objects.all()

    portafolios_completados = Portafolio.objects.filter(id_estado__nombre="Completado")
    portafolios_pendientes = Portafolio.objects.filter(id_estado__nombre="Pendiente")

    context = {
        "titulo": "Mis Portafolios",
        "session": session,
        "persona": persona,
        "redes_sociales": redes_sociales,
        "portafolios_completados": portafolios_completados,
        "portafolios_pendientes": portafolios_pendientes,
    }
    return render(request, 'pages/proyecto/portafollio-Index.html', context)

@check_session
def sobreMi(request, session):
    persona, redes_sociales = obtener_datos_generales()
    aptitudes = Aptitude.objects.all()
    sobremi = Sobremi.objects.first()
    certificados = Certificado.objects.all()

    context = {
        "titulo": "Sobre Mi",
        "session": session,
        "persona": persona,
        "redes_sociales": redes_sociales,
        "aptitudes": aptitudes,
        "sobremi": sobremi,
        "certificados": certificados,
    }
    return render(request, 'pages/sobre-mi/sobre-mi.html', context)


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



def logout(request):
    custom_logout(request)
    return redirect('/')

def enviar_mensaje(request):
    if request.method == 'POST':
        nombre = request.POST.get('nombre', '')
        email = request.POST.get('email', '')
        mensaje = request.POST.get('mensaje', '')
        asunto = request.POST.get('asunto', '')

        errores = []

        if not nombre:
            errores.append('Por favor, ingresa tu nombre.')
        if not email:
            errores.append('Por favor, ingresa tu email.')
        if not mensaje:
            errores.append('Por favor, ingresa tu mensaje.')
        if not asunto:
            errores.append('Por favor, ingresa tu asunto.')

        if errores:
            for error in errores:
                messages.error(request, error)
            return redirect('/#contacto')

        template = render_to_string('pages/contacto/correos.html', {
            'nombre': nombre,
            'email': email,
            'mensaje': mensaje,
        })

        email_message = EmailMessage(
            subject=asunto,
            body=template,
            from_email=settings.EMAIL_HOST_USER,
            to=['i20998785@gmail.com']
        )

        try:
            email_message.send()
            messages.success(request, 'Correo enviado correctamente.')
        except Exception as e:
            messages.error(request, f'Error al enviar el correo: {str(e)}')

        return redirect('/#contacto')

def sorry(request, exception):
    persona = stanley.objects.first()
    context = {
        "titulo": "404",
        "persona": persona,
    }

    return render(request, 'pages/404/404.html', context)
 