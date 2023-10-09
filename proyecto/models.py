from django.db import models
from django.contrib.auth.hashers import make_password

# Create your models here.
class RedSocial(models.Model):
    id_redes = models.AutoField(primary_key=True)
    nombre = models.CharField(max_length=60, null=True)
    enlace = models.URLField( null=True)

class Enlace(models.Model):
    id_enlace = models.AutoField(primary_key=True)
    nombre = models.CharField(max_length=100, null=True)
    url = models.URLField(null=True)


class Aptitude(models.Model):
    id_aptitude = models.AutoField(primary_key=True)
    nombre = models.CharField(max_length=100, null=True)
    
class stanley(models.Model):
    id_persona = models.AutoField(primary_key=True)
    nombre = models.CharField(max_length=60)
    nombre_usuario = models.CharField(max_length=60)
    apellido = models.CharField(max_length=60)
    perfil =   models.ImageField (upload_to='img', null=True, blank=True)
    redes_sociales = models.ManyToManyField(RedSocial )
    password = models.CharField(max_length=128)
   
#    Para Hashar Password
    def save(self, *args, **kwargs):
        if self.password:
            self.password = make_password(self.password)
        super().save(*args, **kwargs)

    def __str__(self):
        return f'{self.nombre} {self.apellido} {self.id_persona}'
    


class Portafolio(models.Model):
    id_portafolio =       models.AutoField(primary_key=True)
    titulo =            models.CharField(max_length=60)
    imagen_portafolio =  models.ImageField (upload_to='img', null=True, blank=True)
    descripcion =       models.CharField(max_length=210)
    rutas_enlaces =       models.ManyToManyField(Enlace)
    aptitudes = models.ManyToManyField(Aptitude )
    
    def __str__(self):
        return str(self.titulo)+" "+str(self.id_portafolio)

class Sobremi(models.Model):
    id_sobremi =       models.AutoField(primary_key=True)
    descripcion_inicio =            models.CharField(max_length=1000, null=True)
    descripcion_aptitude =            models.CharField(max_length=1000)
    descripcion =       models.CharField(max_length=1000)
    aptitudes = models.ManyToManyField(Aptitude )
    
    def __str__(self):
        return str(self.titulo)+" "+str(self.id_sobremi)

class Certificado(models.Model):
    id_certificado = models.AutoField(primary_key=True)
    titulo = models.CharField(max_length=60)
    nombre_escuela = models.CharField(max_length=60)
    imagen_certificado = models.ImageField(upload_to='img', null=True, blank=True)
    enlaces = models.ManyToManyField(Enlace)  
    aptitudes = models.ManyToManyField(Aptitude )

    def __str__(self):
        return self.titulo







