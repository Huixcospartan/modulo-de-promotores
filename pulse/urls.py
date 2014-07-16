from django.conf.urls import patterns, include, url
from django.conf import settings
# Uncomment the next two lines to enable the admin:
from django.contrib import admin
admin.autodiscover()
from django.middleware.csrf import CsrfViewMiddleware

from app.views import EventosDetallesView

urlpatterns = patterns('',
    
    # Para el panel de Aministracion
    url(r'^admin/', include(admin.site.urls)),

    #Estas URL son para el login
    url(r'^$','django.contrib.auth.views.login',{'template_name':'inicio.html'} ,name = 'login'),
    url(r'^cerrar/$' , 'django.contrib.auth.views.logout_then_login', name='logout'),
    
    #Para administrar mis eventos
    url(r'^miseventos/$', 'app.views.miseventos', name='miseventos'),
    url(r'^evento/$', 'app.views.evento', name='evento'),
    url(r'^add/$', 'app.views.add', name='add'),
    
    url(r'^eventosdetalle/(?P<pk>[\d]+)',EventosDetallesView.as_view()),
    url(r'^eventoseliminar/(?P<pk>[\d]+)','app.views.eliminar_evento' , name='evento-delete',),
    url(r'^eventosactualizar/(?P<pk>[\d]+)','app.views.actualizar_evento' , name='evento-update',),
    
    # Accede a registrar un usuario
    url(r'^newuser/$', 'app.views.newuser', name='newuser'),  
   
    # Para editar mi cuenta de usuario
    url(r'^micuenta/$', 'app.views.micuenta', name='micuenta'),
    url(r'^editarmicuenta/$', 'app.views.editar_micuenta', name='editar_micuenta'),
    

    
)
urlpatterns += patterns('',
    url(r'^media/(?P<path>.*)$','django.views.static.serve',{'document_root':settings.MEDIA_ROOT}),
)
