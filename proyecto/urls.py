from django.urls import path
from . import views

urlpatterns = [
    path('', views.index , name='index'),
    # path('login/', views.login_v, name='login'),
    # path('logout/', views.logout_v, name='logout'),
    # path('signup/', views.signup, name='signup'),
    # path('producto/', views.producto , name='producto'),
    # path('comprar/<int:pk>/', views.comprar , name='comprar'),
    # path('verificaCompra/', views.verificaCompra , name='verificaCompra'),
    # path('carrito/<int:producto_pk>', views.carrito, name='carrito'),
    # path('crear', views.crear, name='crear'),
    # path('eliminar/<str:pk>', views.eliminar, name='eliminar'),
    # path('eliminarCarrito/<int:carrito_pk>', views.eliminarCarrito, name='eliminarCarrito'),
    # path('actualizar/<str:pk>', views.actualizar, name='actualizar'),
    # path('productoUpdate/<int:pk>/', views.productoUpdate, name='productoUpdate'),
    # path('vendedor/', views.vendedor , name='vendedor'),
    # path('vendedorIndex/', views.vendedorIndex , name='vendedorIndex'),
    # path('contacto/', views.contacto , name='contacto'),    
    # path('nosotros/', views.nosotros , name='nosotros'),
    # path('sorry/', views.sorry , name='sorry'),
]
