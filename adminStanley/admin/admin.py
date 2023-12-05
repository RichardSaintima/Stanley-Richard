
from django.contrib import admin
from adminStanley.models.models import stanley, Sobremi,Portafolio,Certificado,Aptitude,RedSocial,Estado
# Register your models here.

class personaAdmin(admin.ModelAdmin) :
    list_display =['id_persona',  'nombre_usuario','password']
#     # list_per_page = 2
    list_editable =['password', 'nombre_usuario']

class portafolioAdmin(admin.ModelAdmin) :
    list_display =['id_portafolio', 'titulo', 'imagen_portafolio', 'descripcion','id_estado']  
    # list_filter =['aptitudes']
class sobremiAdmin(admin.ModelAdmin) :
    list_display =['id_sobremi', 'descripcion',] 
#     
class certificadoAdmin(admin.ModelAdmin) :
    list_display =['id_certificado','imagen_certificado', 'nombre_escuela','enlaces_web'] 
#     list_per_page = 10
# 
#     
#     
class aptitudeAdmin(admin.ModelAdmin) :
    list_display =['nombre'] 
#     list_per_page = 10
#     
class estadoAdmin(admin.ModelAdmin) :
    list_display =['nombre'] 
#     list_per_page = 10
#     
    
#     
class redesAdmin(admin.ModelAdmin) :
    list_display =['nombre', 'url'] 
#     list_per_page = 10
    
    

# Register your models here.


admin.site.register(stanley , personaAdmin)
admin.site.register(Portafolio, portafolioAdmin)
admin.site.register(Sobremi, sobremiAdmin)
admin.site.register(Certificado, certificadoAdmin)
admin.site.register(Aptitude, aptitudeAdmin)
admin.site.register(RedSocial, redesAdmin)
admin.site.register(Estado, estadoAdmin)
