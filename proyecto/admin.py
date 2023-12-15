from django.contrib import admin
from adminStanley.models.models import Stanley, Sobremi, Portafolio, Certificado, Aptitude, RedSocial, Estado

class PersonaAdmin(admin.ModelAdmin):
    list_display = ['id_persona', 'nombre_usuario', 'password']
    list_editable = ['password', 'nombre_usuario']

class PortafolioAdmin(admin.ModelAdmin):
    list_display = ['id_portafolio', 'titulo', 'imagen_portafolio', 'descripcion', 'id_estado']

class SobremiAdmin(admin.ModelAdmin):
    list_display = ['id_sobremi', 'descripcion']

class CertificadoAdmin(admin.ModelAdmin):
    list_display = ['id_certificado', 'imagen_certificado', 'nombre_escuela', 'enlaces_web']

class AptitudeAdmin(admin.ModelAdmin):
    list_display = ['nombre']

class EstadoAdmin(admin.ModelAdmin):
    list_display = ['nombre']

class RedesAdmin(admin.ModelAdmin):
    list_display = ['nombre', 'url']

# Register your models here.
admin.site.register(Stanley, PersonaAdmin)
admin.site.register(Portafolio, PortafolioAdmin)
admin.site.register(Sobremi, SobremiAdmin)
admin.site.register(Certificado, CertificadoAdmin)
admin.site.register(Aptitude, AptitudeAdmin)
admin.site.register(RedSocial, RedesAdmin)
admin.site.register(Estado, EstadoAdmin)
