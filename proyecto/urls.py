from django.urls import path
from proyecto.views import views
from adminStanley.views.viewCertificados import agregar_certificado,editar_certificado,eliminar_certificado, stanley_certificado
from adminStanley.views.viewPortafolios import agregar_portafolio,editar_portafolio,eliminar_portafolio, stanley_portafolio
from adminStanley.views.views import agregar_aptitud, agregar_contacto,dashboard, eliminar_aptitud,editar_perfil, dashboard_sobremi

urlpatterns = [
    path('', views.index , name='index'),
    path('#inicio/', views.inicio , name='inicio'),
    path('#hobby/', views.hobby , name='hobby'),
    path('#portafolio/', views.portafolio , name='portafolio'),
    path('#sobre-mi/', views.sobre_mi , name='sobre_mi'),
    path('404/', views.sorry , name='sorry'),
    path('login/', views.login, name='login'),
    path('logout/', views.logout, name='logout'),
    path('dashboard/', dashboard, name='dashboard'),
     path('#enviar_mensaje/', views.enviar_mensaje, name='enviar_mensaje'),


    
# CRETIFICADO
    path('certificado/agregar/', agregar_certificado, name='agregar_certificado'),
    path('certificado/editar/<int:pk>', editar_certificado, name='editar_certificado'),
    path('certificado/eliminar/<str:pk>', eliminar_certificado, name='eliminar_certificado'),
    path('dashboard/certificado/', stanley_certificado, name='stanley_certificado'),

# PORTAFOLIO
    path('dashboard/portafolio/', stanley_portafolio, name='stanley_portafolio'),
    path('portafolio/agregar/', agregar_portafolio, name='agregar_portafolio'),
    path('portafolio/editar/<int:pk>', editar_portafolio, name='editar_portafolio'),
    path('portafolio/eliminar/<str:pk>', eliminar_portafolio, name='eliminar_portafolio'),

    path('dashboard/sobreMi/', dashboard_sobremi, name='dashboard_sobremi'),


    # PERFIL
    path('dashboard/perfil/', editar_perfil, name='editar_perfil'),
    path('dashboard/contacto/', agregar_contacto, name='agregar_contacto'),


#   APTITUDES
    path('dashboard/aptitud/', agregar_aptitud, name='agregar_aptitud'),
    path('dashboard/eliminar_aptitud/<int:aptitud_id>/', eliminar_aptitud, name='eliminar_aptitud'),


]
