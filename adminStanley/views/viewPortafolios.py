from django.shortcuts import render, redirect
from django.contrib import messages
from django.db import transaction
from adminStanley.models.models import  stanley, Portafolio, Aptitude,Estado
from adminStanley.Authenticacion.custom_auth import login_required
from adminStanley.validator.PortafolioValidacion import validate_portafolio_data, validate_portafolio_data_edit


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
    context = {"titulo": "Agregar Portafolio"}
    if request.method == 'POST':
        titulo = request.POST.get('nombre')
        descripcion = request.POST.get('descripcion')
        imagen_portafolio = request.FILES.get('imagen')
        enlaces_web = request.POST.get('enlaces_web') 
        enlaces_github = request.POST.get('enlaces_github')  
        aptitudes = request.POST.getlist('aptitudes')
        id_estado = request.POST.get('id_estado')  

        validation_result = validate_portafolio_data(titulo, imagen_portafolio, descripcion, enlaces_web, enlaces_github,id_estado, aptitudes)
        if validation_result['valid']:
            if id_estado is not None and id_estado.isdigit():
                estado = Estado.objects.get(id_estado=int(id_estado))
                
                portafolio_obj = Portafolio.objects.create(
                    titulo=titulo,
                    imagen_portafolio=imagen_portafolio,
                    descripcion=descripcion,
                    enlaces_web=enlaces_web,
                    enlaces_github=enlaces_github,
                    id_estado=estado,
                )

            portafolio_obj.aptitudes.clear()
            for aptitud_id in aptitudes:
                if not aptitud_id:
                    messages.error(request, 'Error: Aptitud inválida.')
                    return redirect('agregarPortafolio')
                
                try:
                    aptitud = Aptitude.objects.get(id_aptitude=aptitud_id)
                    portafolio_obj.aptitudes.add(aptitud)
                except Aptitude.DoesNotExist:
                    messages.error(request, f'Aptitud con ID {aptitud_id} no encontrada.')
                    return redirect('agregarPortafolio')
                
            messages.success(request, 'Portafolio agregado correctamente.', extra_tags='success')
            return redirect('/stanley/portafolio')
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
    return render(request, 'auth/dashboard/portafolio/crear.html', context)



@login_required
def editarPortafolio(request, pk):
    try:
        portafolio = Portafolio.objects.get(id_portafolio=pk)
    except Portafolio.DoesNotExist:
        messages.error(request, 'Error, Portafolio no existe')
        return redirect('/stanley/portafolio/')
    
    aptitudes = Aptitude.objects.all()
    estados = Estado.objects.all()

    if request.method == "POST":
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

                portafolio.imagen_portafolio = imagen_portafolio if imagen_portafolio is not None else portafolio.imagen_portafolio
                portafolio.titulo = titulo if titulo is not None else portafolio.titulo
                portafolio.descripcion = descripcion if descripcion is not None else portafolio.descripcion
                portafolio.enlaces_web = enlaces_web if enlaces_web is not None else portafolio.enlaces_web
                portafolio.enlaces_github = enlaces_github if enlaces_github is not None else portafolio.enlaces_github
                portafolio.id_estado = estado if estado is not None else portafolio.id_estado

                portafolio.aptitudes.set(aptitudes_ids)

                portafolio.save()

                messages.success(request, 'Portafolio actualizado correctamente.', extra_tags='success')
                return redirect('/stanley/portafolio')
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
