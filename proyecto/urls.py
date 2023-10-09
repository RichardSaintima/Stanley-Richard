from django.urls import path
from . import views
urlpatterns = [
    path('', views.index , name='index'),
    path('hobby/', views.hobby , name='hobby'),
    path('portafolio/', views.portafolio , name='portafolio'),
    path('sobre-mi/', views.sobreMi , name='sobreMi'),
    path('404/', views.sorry , name='sorry'),
    path('stanley/', views.dashboard , name='dashboard'),
    path('login/', views.login, name='login'),
    path('logout/', views.logout, name='logout'),

# CRETIFICADO
    path('stanley/certificado/agregar/', views.agregarCertificado, name='agregarCertificado'),
    path('stanley/certificado/editar/<int:pk>', views.editarCertificado, name='editarCertificado'),
    path('stanley/certificado/eliminar/<str:pk>', views.eliminarCertificado, name='eliminarCertificado'),
    path('stanley/certificado/', views.stanleyCertificado, name='stanleyCertificado'),

# PORTAFOLIO
    path('stanley/portafolio/', views.stanleyPortafolio, name='stanleyPortafolio'),
    path('stanley/portafolio/agregar/', views.agregarPortafolio, name='agregarPortafolio'),
    path('stanley/portafolio/editar/<int:pk>', views.editarPortafolio, name='editarPortafolio'),
    path('stanley/portafolio/eliminar/<str:pk>', views.eliminarPortafolio, name='eliminarPortafolio'),

    path('stanley/sobreMi/', views.stanleySobremi, name='stanleySobremi'),


    # PERFIL
    path('stanley/perfil/', views.perfilEditar, name='perfilEditar'),

    # path('signup/', views.signup, name='signup'),
    # path('producto/', views.producto , name='producto'),
    # path('comprar/<int:pk>/', views.comprar , name='comprar'),
    # path('verificaCompra/', views.verificaCompra , name='verificaCompra'),
    # path('carrito/<int:producto_pk>', views.carrito, name='carrito'),
    # path('crear', views.crear, name='crear'),
    # path('eliminarCarrito/<int:carrito_pk>', views.eliminarCarrito, name='eliminarCarrito'),
    # path('actualizar/<str:pk>', views.actualizar, name='actualizar'),
    # path('productoUpdate/<int:pk>/', views.productoUpdate, name='productoUpdate'),
    # path('vendedor/', views.vendedor , name='vendedor'),
    # path('vendedorIndex/', views.vendedorIndex , name='vendedorIndex'),
    # path('contacto/', views.contacto , name='contacto'),    
    # path('nosotros/', views.nosotros , name='nosotros'),
    # path('sorry/', views.sorry , name='sorry'),
]
