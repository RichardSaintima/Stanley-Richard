from django.urls import path
from adminStanley.views import views, viewCertificados,viewPortafolios

urlpatterns = [
    
# CRETIFICADO
    path('certificado/agregar/', viewCertificados.agregar_certificado, name='agregar_certificado'),
    path('certificado/editar/<int:pk>', viewCertificados.editar_certificado, name='editar_certificado'),
    path('certificado/eliminar/<str:pk>', viewCertificados.eliminar_certificado, name='eliminar_certificado'),
    path('dashboard/certificado/', viewCertificados.stanley_certificado, name='stanley_certificado'),

# PORTAFOLIO
    path('dashboard/portafolio/', viewPortafolios.stanley_portafolio, name='stanley_portafolio'),
    path('portafolio/agregar/', viewPortafolios.agregar_portafolio, name='agregar_portafolio'),
    path('portafolio/editar/<int:pk>', viewPortafolios.editar_portafolio, name='editar_portafolio'),
    path('portafolio/eliminar/<str:pk>', viewPortafolios.eliminar_portafolio, name='eliminar_portafolio'),

    path('dashboard/sobreMi/', views.dashboard_sobremi, name='dashboard_sobremi'),


    # PERFIL
    path('dashboard/perfil/', views.editar_perfil, name='editar_perfil'),
    path('dashboard/contacto/', views.agregar_contacto, name='agregar_contacto'),

#   APTITUDES
    path('dashboard/aptitud/', views.agregar_aptitud, name='agregar_aptitud'),
    path('dashboard/eliminar_aptitud/<int:aptitud_id>', views.eliminar_aptitud, name='eliminar_aptitud'),

]
