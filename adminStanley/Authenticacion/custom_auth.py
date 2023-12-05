from adminStanley.models.models import stanley
from django.shortcuts import render, redirect, reverse
from django.contrib import messages

from django.contrib.auth.hashers import check_password

def custom_authenticate(nombre_usuario, password):
    try:
        persona = stanley.objects.get(nombre_usuario=nombre_usuario)
        if check_password(password, persona.password):
            return persona
    except stanley.DoesNotExist:
        pass
    return None



def custom_login(request, persona):
    if persona is not None:
        request.session['id_persona'] = persona.id_persona
    else:
        messages.error(request, 'Verifica tu contraseña.')
        return redirect('login/')

def custom_logout(request):
    request.session.flush()
    request.session.clear()
    request.session.modified = True
    return redirect('/')


def login_required(view_func):
    def wrapper(request, *args, **kwargs):
        if 'id_persona' not in request.session:
            messages.error(request, 'Debes iniciar sesión para acceder.')
            return redirect('/login/')
        
        return view_func(request, *args, **kwargs)

    return wrapper