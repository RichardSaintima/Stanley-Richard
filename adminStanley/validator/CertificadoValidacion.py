from adminStanley.models.models import Aptitude
from django.contrib import messages


def validate_certificado_data(titulo, nombre_escuela, imagen_certificado, enlaces_web, aptitudes):
    validation_result = {'valid': True, 'errors': []}

    if not titulo:
        validation_result['valid'] = False
        validation_result['errors'].append('El campo de título es obligatorio.')

    if not nombre_escuela:
        validation_result['valid'] = False
        validation_result['errors'].append('El campo de Nombre escuela es obligatorio.')

    if not imagen_certificado:
        validation_result['valid'] = False
        validation_result['errors'].append('Debe seleccionar una imagen.')

    if not enlaces_web:
        validation_result['valid'] = False
        validation_result['errors'].append('Debe proporcionar  un enlace.')

    if not aptitudes:
        validation_result['valid'] = False
        validation_result['errors'].append('Debe seleccionar al menos una aptitud.')

    return validation_result


# validacion para editar certificado
def validate_certificado_data_edit(titulo, nombre_escuela,  enlaces_web,  aptitudes):
    validation_result = {'valid': True, 'errors': []}

    if not titulo:
        validation_result['valid'] = False
        validation_result['errors'].append('El campo de título es obligatorio.')

    if not nombre_escuela:
        validation_result['valid'] = False
        validation_result['errors'].append('El campo de Nombre escuela es obligatorio.')

    if not enlaces_web:
        validation_result['valid'] = False
        validation_result['errors'].append('Debe proporcionar  un enlace.')

    if not aptitudes:
        validation_result['valid'] = False
        validation_result['errors'].append('Debe seleccionar al menos una aptitud.')

    return validation_result