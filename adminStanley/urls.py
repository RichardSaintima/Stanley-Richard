from django.urls import path
from adminStanley.views import views, viewCertificados,viewPortafolios

urlpatterns = [
    
# CRETIFICADO
    path('stanley/certificado/agregar/', viewCertificados.agregarCertificado, name='agregarCertificado'),
    path('stanley/certificado/editar/<int:pk>', viewCertificados.editarCertificado, name='editarCertificado'),
    path('stanley/certificado/eliminar/<str:pk>', viewCertificados.eliminarCertificado, name='eliminarCertificado'),
    path('stanley/certificado/', viewCertificados.stanleyCertificado, name='stanleyCertificado'),

# PORTAFOLIO
    path('stanley/portafolio/', viewPortafolios.stanleyPortafolio, name='stanleyPortafolio'),
    path('stanley/portafolio/agregar/', viewPortafolios.agregarPortafolio, name='agregarPortafolio'),
    path('stanley/portafolio/editar/<int:pk>', viewPortafolios.editarPortafolio, name='editarPortafolio'),
    path('stanley/portafolio/eliminar/<str:pk>', viewPortafolios.eliminarPortafolio, name='eliminarPortafolio'),

    path('stanley/sobreMi/', views.stanleySobremi, name='stanleySobremi'),


    # PERFIL
    path('stanley/perfil/', views.perfilEditar, name='perfilEditar'),
    path('stanley/contacto/', views.agregarContacto, name='agregarContacto'),

#   APTITUDES
    path('stanley/aptitud/', views.agregarAptitud, name='agregarAptitud'),
    path('stanley/eliminar_aptitud/<int:aptitud_id>', views.eliminar_aptitud, name='eliminar_aptitud'),

]
