
from django.contrib import admin
from proyecto.models import stanley, Sobremi,Portafolio,Certificado,Aptitude,Enlace
# Register your models here.

class personaAdmin(admin.ModelAdmin) :
    list_display =['id_persona', 'nombre', 'apellido',  'nombre_usuario','password']
#     # list_per_page = 2
    list_editable =['password', 'nombre']

class portafolioAdmin(admin.ModelAdmin) :
    list_display =['id_portafolio', 'titulo', 'imagen_portafolio', 'descripcion']  
#     # list_filter =['id_portafolio']
class sobremiAdmin(admin.ModelAdmin) :
    list_display =['id_sobremi', 'descripcion',] 
#     
class certificadoAdmin(admin.ModelAdmin) :
    list_display =['id_certificado','imagen_certificado', 'nombre_escuela'] 
#     list_per_page = 10
#     
#     
class enlacesAdmin(admin.ModelAdmin) :
    list_display =['nombre','url'] 
#     list_per_page = 10
#     
#     
class aptitudeAdmin(admin.ModelAdmin) :
    list_display =['nombre'] 
#     list_per_page = 10
#     
    

# Register your models here.


admin.site.register(stanley , personaAdmin)
admin.site.register(Portafolio, portafolioAdmin)
admin.site.register(Sobremi, sobremiAdmin)
admin.site.register(Certificado, certificadoAdmin)
admin.site.register(Aptitude, aptitudeAdmin)
