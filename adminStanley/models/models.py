from django.db import models
from django.contrib.auth.hashers import make_password

# Create your models here.
class RedSocial(models.Model):
    nombre = models.CharField(max_length=20)
    icono = models.CharField(max_length=50)
    url = models.URLField()
class Estado(models.Model):
    id_estado =         models.AutoField(db_column='idEstado', primary_key=True)
    nombre =            models.CharField(max_length=20, blank=False, null=False)
    def __str__(self):
        return str(self.nombre)


class Aptitude(models.Model):
    id_aptitude = models.AutoField(primary_key=True)
    nombre = models.CharField(max_length=100)
    
    
class stanley(models.Model):
    id_persona = models.AutoField(primary_key=True)
    nombre_usuario = models.CharField(max_length=60)
    perfil =   models.ImageField (upload_to='img', null=True, blank=True)
    redes_sociales = models.ManyToManyField(RedSocial)
    password = models.CharField(max_length=128)
   
    def save(self, *args, **kwargs):
        if self.password:
            self.password = make_password(self.password)
        super().save(*args, **kwargs)

    def __str__(self):
        return f'{self.nombre_usuario}  {self.id_persona}'

class Portafolio(models.Model):
    id_portafolio =       models.AutoField(primary_key=True)
    titulo =            models.CharField(max_length=60)
    imagen_portafolio =  models.ImageField (upload_to='img', null=True, blank=True)
    descripcion =       models.CharField(max_length=210)
    aptitudes =         models.ManyToManyField(Aptitude)
    enlaces_web =       models.URLField(null=True, blank=True)
    enlaces_github =    models.URLField(null=True, blank=True)
    id_estado = models.ForeignKey('Estado', on_delete=models.CASCADE, db_column='idEstado', null=True)
    
    
    def __str__(self):
        return str(self.titulo)+" "+str(self.id_portafolio)

class Sobremi(models.Model):
    id_sobremi = models.AutoField(primary_key=True)
    descripcion_inicio = models.TextField(null=True, blank=True)
    descripcion = models.TextField()

    def __str__(self):
        return f"Sobre Mí - {self.id}"


class Certificado(models.Model):
    id_certificado = models.AutoField(primary_key=True)
    titulo = models.CharField(max_length=60)
    nombre_escuela = models.CharField(max_length=60)
    imagen_certificado = models.ImageField(upload_to='img', null=True, blank=True) 
    enlaces_web = models.URLField()
    aptitudes = models.ManyToManyField(Aptitude) 
    def __str__(self):
        return self.titulo



