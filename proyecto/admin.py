from django.contrib import admin
from adminStanley.models.models import stanley, Sobremi, Portafolio, Certificado, Aptitude, RedSocial, Estado

class personaAdmin(admin.ModelAdmin):
    list_display = ['id_persona', 'nombre_usuario', 'password']
    list_editable = ['password', 'nombre_usuario']

class portafolioAdmin(admin.ModelAdmin):
    list_display = ['id_portafolio', 'titulo', 'imagen_portafolio', 'descripcion', 'id_estado']

class sobremiAdmin(admin.ModelAdmin):
    list_display = ['id_sobremi', 'descripcion']

class certificadoAdmin(admin.ModelAdmin):
    list_display = ['id_certificado', 'imagen_certificado', 'nombre_escuela', 'enlaces_web']
    

class aptitudeAdmin(admin.ModelAdmin):
    list_display = ['nombre']

class estadoAdmin(admin.ModelAdmin):
    list_display = ['nombre']
class redesAdmin(admin.ModelAdmin):
    list_display = ['nombre', 'url']

# Register your models here.
admin.site.register(stanley, personaAdmin)
admin.site.register(Portafolio, portafolioAdmin)
admin.site.register(Sobremi, sobremiAdmin)
admin.site.register(Certificado, certificadoAdmin)
admin.site.register(Aptitude, aptitudeAdmin)
admin.site.register(RedSocial, redesAdmin)
admin.site.register(Estado, estadoAdmin)
