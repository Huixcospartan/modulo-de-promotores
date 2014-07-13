from django.contrib import admin
from models import *

class ClienteAdmin(admin.ModelAdmin):
	list_display=('id','nombre','apellidos','fechanacimiento','genero','email','password','activo')
	list_filter =('nombre','apellidos','fechanacimiento','genero','activo')
	search_fields = ('nombre','apellidos','email',)
	list_editable=('nombre','apellidos','fechanacimiento','genero')

class AcademiaAdmin(admin.ModelAdmin):
	list_display=('id','academica','areaestudio','congresos','convenciones','seminarios','talleres','diplomados','cursos','conferencias','expos','cliente',)
	

class DestinoAdmin(admin.ModelAdmin):
	list_display=('id','calle','codigopostal')
	list_filter =('codigopostal',)
	search_fields =('calle','codigopostal')
	list_editable=('calle','codigopostal')

class TipoEventoAdmin(admin.ModelAdmin):
	list_display=('id','nombretipoevento','detallesevento')
	list_filter =('nombretipoevento',)
	search_fields =('nombretipoevento',)
	list_editable=('nombretipoevento','detallesevento')

class EventoAdmin(admin.ModelAdmin):
	list_display=('id','titulo','descripcipn','Promotor','fechaevento','hora','tipoevento','costo','destino','activo','imagen','evento_imagen',)
	list_filter =('titulo',)
	search_fields =('titulo','descripcipn')
	list_editable=('titulo','descripcipn','fechaevento','hora','tipoevento','costo','destino','activo','imagen')

class CalendarioAdmin(admin.ModelAdmin):
	list_display=('id','fecha','evento','cliente')
	list_filter =('fecha',)
	search_fields =('evento','cliente',)
	list_editable=('fecha','evento','cliente')

class OrigenAdmin(admin.ModelAdmin):
	list_display=('id','calle')
	list_filter =('calle',)
	search_fields =('calle',)
	list_editable=('calle',)

class RutaAdmin(admin.ModelAdmin):
	list_display=('id','logitud','latitud','destino','origen')
	list_editable=('logitud','latitud','destino','origen')

class EntretenimientoAdmin(admin.ModelAdmin):
	list_display=('id','entretenimiento','conciertos','electronica','jazzblues','trova','rock','alternativa','gruperanortena','infantil','hiphop','ranchera','pop','metal','reague','reggeatton','baladasboleros','salsacumbia','cristiana','deportes',
	 'futbol','basquetball','tenis','beisball','volleyball','torneos','maratones','autosmotos','futbolAmericano','artesMarciales','box','luchaLibre','atletismo','toros','baresantros','inaguracion','promocion','show','fiestasTematicas','bienvenida','cliente')
	
class CulturalAdmin(admin.ModelAdmin):
	list_display=('id','cultural','balletdanza','teatro','comedia','drama','infantilC','musical','otrosT','circos','exposiciones','fotografia','escultura','pintura','libros','otrosE','cineArte','musica','clasica','instrumental','folklorepopular','turistico','ferias','carnavales',
		'peregrinaciones','fiestasReligiosasIndigenas','otrosTuristica','cliente')
	
#class preferenciaAdmin(admin.ModelAdmin):
	#list_display=('id','cliente')
	#list_editable=('cliente',)

class promotorAdmin(admin.ModelAdmin):
	list_display=('id','nombre','paterno','materno','usuario')#'username')
	list_editable=('nombre','nombre','paterno','materno','usuario')



admin.site.register(Academia,AcademiaAdmin)
admin.site.register(Destino,DestinoAdmin)
admin.site.register(TipoEvento,TipoEventoAdmin)
admin.site.register(Evento,EventoAdmin)
admin.site.register(Calendario,CalendarioAdmin)
admin.site.register(Origen,OrigenAdmin)
admin.site.register(Ruta,RutaAdmin)
admin.site.register(Entretenimiento,EntretenimientoAdmin)
admin.site.register(Cultural,CulturalAdmin)
admin.site.register(Cliente,ClienteAdmin)
#admin.site.register(Preferencia,preferenciaAdmin)
admin.site.register(Promotor,promotorAdmin)