from __future__ import unicode_literals
from django.db import models
from django.contrib.auth.models import User

class Promotor(models.Model):
    nombre   = models.CharField(max_length = 45)
    paterno  = models.CharField(max_length = 45)
    materno  = models.CharField(max_length = 45)
    usuario  = models.OneToOneField(User)
    #usuario  = models.ForeignKey(User) 
    #username = models.CharField(max_length = 45)
    
    def __unicode__(self):
      return str(self.usuario)   
    
class Destino(models.Model):
    calle        = models.CharField(max_length = 45)
    codigopostal = models.IntegerField(default=0)
    
    def __unicode__(self):
        return "%s" % (self.calle)
        
class TipoEvento(models.Model):
    tipoevento    = models.CharField(('Tipo de Evento'),max_length = 45)
    detallesevento    = models.CharField(('Detalles del Evento'),max_length = 45)

    def __unicode__(self):
        return self.tipoevento+' - '+self.detallesevento
   

class Evento(models.Model):
    titulo      = models.CharField(max_length = 45)
    descripcipn = models.TextField(('Descripcion'), max_length = 45)
    fechaevento = models.DateField(('Fecha de Evento'),auto_now_add=False)
    hora        = models.TimeField(auto_now_add=False)
    tipoevento  = models.ForeignKey(TipoEvento)
    Promotor    = models.ForeignKey(Promotor)
    costo       = models.FloatField()
    destino     = models.ForeignKey(Destino)
    activo      = models.BooleanField(default=True)
    imagen      = models.ImageField(upload_to='img')

    def __unicode__(self):
      return self.titulo

    def evento_imagen(self):
      return """
        <img src="%s" />
      """%self.imagen.url
    evento_imagen.allow_tags = True
    evento_imagen.admin_order_field ='imagen'

    def imagenevento(self):
      return self.imagen.url
    evento_imagen.allow_tags = True
    evento_imagen.admin_order_field ='imagen'
    
    def costoevento(self):
      if self.costo == 0:
        return 'Gratis'
      else:
        return "$ %s"%self.costo

class Cliente(models.Model):

    SEXO_CHOICES = (
    ('','---- Seleccione ---'),
    ('m','Masculino'),
    ('f','Femenino'),
    )

    nombre          = models.CharField(max_length = 20)
    apellidos       = models.CharField(max_length = 45)
    fechanacimiento = models.DateField(('Fecha de Nacimiento'),auto_now_add=False)
    genero          = models.CharField(max_length=1, choices=SEXO_CHOICES,default=SEXO_CHOICES)
    email           = models.EmailField(max_length=75)
    password        = models.CharField(max_length = 45)
    activo          = models.BooleanField(default=True)
      
    def __unicode__(self):
        return str(self.nombre)
    

class Calendario(models.Model):
    fecha       = models.DateTimeField(auto_now_add=False)
    evento      = models.ForeignKey(Evento)
    cliente     = models.ForeignKey(Cliente)
  
    def __unicode__(self):
        return "%s" % (self.fecha)

class Origen(models.Model):
    calle = models.CharField(max_length = 45)

    def __unicode__(self):
        return self.calle


class Ruta(models.Model):
    logitud = models.FloatField()
    latitud = models.FloatField()
    destino = models.ForeignKey(Destino)
    origen  = models.ForeignKey(Origen)

    def __unicode__(self):
        return "%s" % (self.logitud)

class Preferencia(models.Model):
	identifcador = models.IntegerField()
  
class ClientePreferencia(models.Model):
  cliente     = models.ForeignKey(Cliente)
  preferencia = models.ForeignKey(Preferencia)

     
class Academia(models.Model):
  academica 	   = models.BooleanField(default=True)
  areaestudio 	 = models.BooleanField(default=True)
  congresos 	   = models.BooleanField(default=True)
  convenciones 	 = models.BooleanField(default=True)
  seminarios	   = models.BooleanField(default=True)
  talleres 		   = models.BooleanField(default=True)
  diplomados	   = models.BooleanField(default=True)
  cursos 		     = models.BooleanField(default=True)
  conferencias	 = models.BooleanField(default=True)
  expos 		     = models.BooleanField(default=True)
  cliente	       = models.ForeignKey(Cliente)

  def __unicode__(self):
        return u"%s Academia" % self.academica

class Entretenimiento(models.Model):
    entretenimiento     =  models.BooleanField(default=True)
    conciertos          =  models.BooleanField(default=True)
    electronica         =  models.BooleanField(default=True)
    jazzblues           =  models.BooleanField(default=True)
    trova               =  models.BooleanField(default=True)
    rock                =  models.BooleanField(default=True)
    alternativa         =  models.BooleanField(default=True)
    gruperanortena      =  models.BooleanField(default=True)
    infantil            =  models.BooleanField(default=True)
    hiphop              =  models.BooleanField(default=True)
    ranchera            =  models.BooleanField(default=True)
    pop                 =  models.BooleanField(default=True)
    metal               =  models.BooleanField(default=True)
    reague              =  models.BooleanField(default=True)
    reggeatton          =  models.BooleanField(default=True)
    baladasboleros      =  models.BooleanField(default=True)
    salsacumbia         =  models.BooleanField(default=True)
    cristiana           =  models.BooleanField(default=True)
    deportes            =  models.BooleanField(default=True)
    futbol              =  models.BooleanField(default=True)
    basquetball         =  models.BooleanField(default=True)
    tenis               =  models.BooleanField(default=True)
    beisball            =  models.BooleanField(default=True)
    volleyball          =  models.BooleanField(default=True)
    torneos             =  models.BooleanField(default=True)
    maratones           =  models.BooleanField(default=True)
    autosmotos          =  models.BooleanField(default=True)
    futbolAmericano     =  models.BooleanField(default=True)
    artesMarciales      =  models.BooleanField(default=True)
    box                 =  models.BooleanField(default=True)
    luchaLibre          =  models.BooleanField(default=True)
    atletismo           =  models.BooleanField(default=True)
    toros               =  models.BooleanField(default=True)
    baresantros         =  models.BooleanField(default=True)
    inaguracion         =  models.BooleanField(default=True)
    promocion           =  models.BooleanField(default=True)
    show                =  models.BooleanField(default=True)
    fiestasTematicas    =  models.BooleanField(default=True)
    bienvenida          =  models.BooleanField(default=True)
    cliente	            = models.ForeignKey(Cliente)
    def __unicode__(self):
        return u"%s Entretenimiento" % self.entretenimiento

        
class Cultural(models.Model):
   cultural                     =  models.BooleanField(default=True)
   balletdanza                  =  models.BooleanField(default=True)
   teatro                       =  models.BooleanField(default=True)
   comedia                      =  models.BooleanField(default=True)
   drama                        =  models.BooleanField(default=True)
   infantilC                    =  models.BooleanField(default=True)
   musical                      =  models.BooleanField(default=True)
   otrosT                       =  models.BooleanField(default=True)
   circos                       =  models.BooleanField(default=True) 
   exposiciones                 =  models.BooleanField(default=True)
   fotografia                   =  models.BooleanField(default=True)
   escultura                    =  models.BooleanField(default=True)
   pintura                      =  models.BooleanField(default=True)
   libros                       =  models.BooleanField(default=True)
   otrosE                       =  models.BooleanField(default=True)
   cineArte                     =  models.BooleanField(default=True)
   musica                       =  models.BooleanField(default=True)
   clasica                      =  models.BooleanField(default=True)
   instrumental                 =  models.BooleanField(default=True)
   folklorepopular              =  models.BooleanField(default=True)
   turistico                    =  models.BooleanField(default=True)
   ferias                       =  models.BooleanField(default=True)
   carnavales                   =  models.BooleanField(default=True)
   peregrinaciones              =  models.BooleanField(default=True)
   fiestasReligiosasIndigenas   =  models.BooleanField(default=True)
   otrosTuristica               =  models.BooleanField(default=True)
   cliente	                    = models.ForeignKey(Cliente)

   def __unicode__(self):
        return u"%s Cultural" % self.cultural


