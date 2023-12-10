from adminStanley.models.models import stanley

def check_session(view_func):
    def wrapper(request):
        session = None
        if 'id_persona' in request.session:
            id_persona = request.session['id_persona']
            session = stanley.objects.get(id_persona=id_persona)
            
        return view_func(request, session)
    return wrapper
