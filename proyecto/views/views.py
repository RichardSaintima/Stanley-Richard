from django.shortcuts import render, redirect
from django.contrib import messages
from adminStanley.models.models import Estado, Sobremi, stanley, Certificado, Aptitude,Portafolio
from datetime import datetime
from proyecto.Authenticacion.custom_auth import check_session, custom_authenticate, custom_login, custom_logout, login_required

@check_session
def index(request, session):
    persona = stanley.objects.first() 
    redes_sociales = persona.redes_sociales.all()
    sobremi = Sobremi.objects.first()
    context = {
        "titulo": "Inicio",
        "persona": persona,
        "session": session,
        "redes_sociales": redes_sociales,
        "sobremi": sobremi,
    }
    return render(request, 'pages/start/index.html', context)




@check_session
def hobby(request, session):
    persona = stanley.objects.first()
    redes_sociales = persona.redes_sociales.all()
    context = {
        "titulo": "Hobby",
        "session": session,
        "persona": persona,
        "redes_sociales": redes_sociales,
    }
    return render(request, 'pages/hobby/blog.html',context)


@check_session
def portafolio(request, session):
    persona = stanley.objects.first()
    redes_sociales = persona.redes_sociales.all()
    estados = Estado.objects.all()
    
    portafolios_completados = Portafolio.objects.filter(id_estado__nombre="Completado")
    portafolios_en_curso = Portafolio.objects.filter(id_estado__nombre="EnCurso")
    portafolios_pendientes = Portafolio.objects.filter(id_estado__nombre="Pendiente")

    context = {
        "titulo": "Portafolio",
        "session": session,
        "persona": persona,
        "redes_sociales": redes_sociales,
        "portafolios_completados": portafolios_completados,
        "portafolios_en_curso": portafolios_en_curso,
        "portafolios_pendientes": portafolios_pendientes,
    }
    return render(request, 'pages/proyecto/portafollio-Index.html', context)



@check_session
def sobreMi(request, session):
    persona = stanley.objects.first()
    aptitudes = Aptitude.objects.all()
    sobremi = Sobremi.objects.first()
    redes_sociales = persona.redes_sociales.all()
    fecha_nacimiento = datetime(1999, 4, 8)
    fecha_actual = datetime.now()
    diferencia = fecha_actual - fecha_nacimiento
    edad = diferencia.days // 365
    certificados = Certificado.objects.all()
    
    context = {
        "titulo": "Sobre Mi",
        "session": session,
        "edad": edad,
        "persona": persona,
        "redes_sociales": redes_sociales,
        "aptitudes": aptitudes,
        "sobremi": sobremi,
        "certificados": certificados,
        
    }
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



def logout(request):
    custom_logout(request)
    return redirect('/')


def sorry(request, exception):
    # return HttpResponse("Lo sentimos pero la página que buscas no existe")
    persona = stanley.objects.first()
    context = {
        "titulo": "404",
        "persona": persona,
    }

    return render(request, 'pages/404/404.html', context)
 