def validate_certificado_data(titulo, nombre_escuela, imagen_certificado, enlaces, aptitudes):
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

    if not enlaces:
        validation_result['valid'] = False
        validation_result['errors'].append('Debe proporcionar al menos un enlace.')

    if not aptitudes:
        validation_result['valid'] = False
        validation_result['errors'].append('Debe seleccionar al menos una aptitud.')

    return validation_result



def validate_portafolio_data(titulo, imagen_portafolio, descripcion, rutas_enlaces, aptitudes):
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

    if not rutas_enlaces:
        validation_result['valid'] = False
        validation_result['errors'].append('Debe proporcionar al menos un enlace.')

    if not aptitudes:
        validation_result['valid'] = False
        validation_result['errors'].append('Debe seleccionar al menos una aptitud.')

    return validation_result


def validate_sobremi_data(descripcion_inicio, descripcion_aptitude, descripcion, aptitudes):
    validation_result = {'valid': True, 'errors': []}

    if not descripcion_inicio:
        validation_result['valid'] = False
        validation_result['errors'].append('El campo de descripción de inicio es obligatorio.')

    if not descripcion_aptitude:
        validation_result['valid'] = False
        validation_result['errors'].append('El campo de descripción de aptitudes es obligatorio.')

    if not descripcion:
        validation_result['valid'] = False
        validation_result['errors'].append('El campo de descripción es obligatorio.')

    if not aptitudes:
        validation_result['valid'] = False
        validation_result['errors'].append('Debe seleccionar al menos una aptitud.')

    return validation_result

# validacion para editar portafolio
def validate_portafolio_data_edit(titulo, descripcion, rutas_enlaces, aptitudes):
    validation_result = {'valid': True, 'errors': []}

    if not titulo:
        validation_result['valid'] = False
        validation_result['errors'].append('El campo de título es obligatorio.')

    if not descripcion:
        validation_result['valid'] = False
        validation_result['errors'].append('Debe proporcionar una descripción.')

    if not rutas_enlaces:
        validation_result['valid'] = False
        validation_result['errors'].append('Debe proporcionar al menos un enlace.')

    if not aptitudes:
        validation_result['valid'] = False
        validation_result['errors'].append('Debe seleccionar al menos una aptitud.')

    return validation_result

# validacion para editar certificado
def validate_certificado_data_edit(titulo, nombre_escuela, enlaces, aptitudes):
    validation_result = {'valid': True, 'errors': []}

    if not titulo:
        validation_result['valid'] = False
        validation_result['errors'].append('El campo de título es obligatorio.')

    if not nombre_escuela:
        validation_result['valid'] = False
        validation_result['errors'].append('El campo de Nombre escuela es obligatorio.')

    if not enlaces:
        validation_result['valid'] = False
        validation_result['errors'].append('Debe proporcionar al menos un enlace.')

    if not aptitudes:
        validation_result['valid'] = False
        validation_result['errors'].append('Debe seleccionar al menos una aptitud.')

    return validation_result