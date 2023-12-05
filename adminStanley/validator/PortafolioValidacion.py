from django.urls import path
from adminStanley.views import views, viewCertificados,viewPortafolios

def validate_portafolio_data(titulo,imagen_portafolio, descripcion, enlaces_web, enlaces_github,id_estado, aptitudes):
    validation_result = {'valid': True, 'errors': []}

    if not titulo:
        validation_result['valid'] = False
        validation_result['errors'].append('El campo de título es obligatorio.')

    if not imagen_portafolio:
        validation_result['valid'] = False
        validation_result['errors'].append('Debe seleccionar una imagen.')

    if not descripcion:
        validation_result['valid'] = False
        validation_result['errors'].append('Debe proporcionar una descripción.')

    if not enlaces_web and not enlaces_github:
        validation_result['valid'] = False
        validation_result['errors'].append('Debe proporcionar al menos un enlace web o un enlace GitHub.')

    if not aptitudes:
        validation_result['valid'] = False
        validation_result['errors'].append('Debe seleccionar al menos una aptitud.')

    if not id_estado:
        validation_result['valid'] = False
        validation_result['errors'].append('Debe poner el estado.')

    return validation_result


# validacion para editar portafolio
def validate_portafolio_data_edit(titulo, descripcion, enlaces_web, enlaces_github, aptitudes):
    validation_result = {'valid': True, 'errors': []}

    if not titulo:
        validation_result['valid'] = False
        validation_result['errors'].append('El campo de título es obligatorio.')

    if not descripcion:
        validation_result['valid'] = False
        validation_result['errors'].append('Debe proporcionar una descripción.')

    if not enlaces_web and not enlaces_github:
        validation_result['valid'] = False
        validation_result['errors'].append('Debe proporcionar al menos un enlace web o un enlace GitHub.')

    if not aptitudes:
        validation_result['valid'] = False
        validation_result['errors'].append('Debe seleccionar al menos una aptitud.')

    return validation_result