

from adminStanley.models.models import Aptitude
from django.contrib import messages








def validate_sobremi_data(descripcion_inicio, descripcion):
    validation_result = {'valid': True, 'errors': []}

    if not descripcion_inicio:
        validation_result['valid'] = False
        validation_result['errors'].append('El campo de descripción de inicio es obligatorio.')

    if not descripcion:
        validation_result['valid'] = False
        validation_result['errors'].append('El campo de descripción es obligatorio.')

    return validation_result






