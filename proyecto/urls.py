from django.urls import path
from proyecto.views import views
from adminStanley.views.viewCertificados import agregarCertificado,editarCertificado,eliminarCertificado, stanleyCertificado
from adminStanley.views.viewPortafolios import agregarPortafolio,editarPortafolio,eliminarPortafolio, stanleyPortafolio
from adminStanley.views.views import agregarAptitud, agregarContacto,dashboard, eliminar_aptitud,perfilEditar, stanleySobremi

urlpatterns = [
    path('', views.index , name='index'),
    path('hobby/', views.hobby , name='hobby'),
    path('portafolio/', views.portafolio , name='portafolio'),
    path('sobre-mi/', views.sobreMi , name='sobreMi'),
    path('404/', views.sorry , name='sorry'),
    path('login/', views.login, name='login'),
    path('logout/', views.logout, name='logout'),
    path('stanley/', dashboard, name='dashboard'),


    
# CRETIFICADO
    path('stanley/certificado/agregar/', agregarCertificado, name='agregarCertificado'),
    path('stanley/certificado/editar/<int:pk>', editarCertificado, name='editarCertificado'),
    path('stanley/certificado/eliminar/<str:pk>', eliminarCertificado, name='eliminarCertificado'),
    path('stanley/certificado/', stanleyCertificado, name='stanleyCertificado'),

# PORTAFOLIO
    path('stanley/portafolio/', stanleyPortafolio, name='stanleyPortafolio'),
    path('stanley/portafolio/agregar/', agregarPortafolio, name='agregarPortafolio'),
    path('stanley/portafolio/editar/<int:pk>', editarPortafolio, name='editarPortafolio'),
    path('stanley/portafolio/eliminar/<str:pk>', eliminarPortafolio, name='eliminarPortafolio'),

    path('stanley/sobreMi/', stanleySobremi, name='stanleySobremi'),


    # PERFIL
    path('stanley/perfil/', perfilEditar, name='perfilEditar'),
    path('stanley/contacto/', agregarContacto, name='perfilEditar'),


#   APTITUDES
    path('stanley/aptitud/', agregarAptitud, name='agregarAptitud'),
    path('stanley/eliminar_aptitud/<int:aptitud_id>/', eliminar_aptitud, name='eliminar_aptitud'),


]
