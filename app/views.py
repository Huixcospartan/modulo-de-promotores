from django.views.generic import TemplateView,FormView
from django.shortcuts import render_to_response,get_object_or_404
from django.template.context import RequestContext
from forms import * 
from django.http import HttpResponse,HttpResponseRedirect, HttpResponseForbidden
from django.contrib.auth.decorators import login_required
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth import login, authenticate, logout
from models import * 

def newuser(request):
    template ='registrarse.html'
    if request.method=='POST':
        formulario = UserForm(request.POST)
        if formulario.is_valid:
            #import ipdb; ipdb.set_trace()
            usuario             = formulario.save(commit=True)
            promotor            = Promotor()
            promotor.nombre     = formulario.cleaned_data['nombre']
            promotor.paterno    = formulario.cleaned_data['paterno']
            promotor.materno    = formulario.cleaned_data['materno']
            promotor.usuario    = usuario
            promotor.save()
            #promotor.username   = formulario.cleaned_data['username']
            #formulario.save()
            return HttpResponseRedirect('/')
    else:
        formulario = UserForm()
    return render_to_response(template,locals(), context_instance=RequestContext(request))
    

@login_required
def evento(request):    
    #import ipdb; ipdb.set_trace()
    evento = Evento.objects.all()
    #promotor = User.objects.get(id=request.user.id)
    #evento = get_object_or_404(Evento,pk =2 ) #User.objects.get(id=request.user.id).id)    
    template = "eventos.html"
    return render_to_response(template,locals())

@login_required
def micuenta(request):
    #import ipdb; ipdb.set_trace()
    usuario  = User.objects.get(username=request.user.username)
    promotor = Promotor.objects.get(usuario=request.user.id)
    template = "micuenta.html"
    return render_to_response(template,locals())

@login_required
def miseventos(request):
    #import ipdb; ipdb.set_trace()
    promotor = Promotor.objects.get(usuario=request.user.id)
    evento   = Evento.objects.filter(Promotor=promotor)
    template = "miseventos.html"
    return render_to_response(template,locals())

# http://blog.byjakt.com/multiple-django-forms-in-one-form.html
# http://stackoverflow.com/questions/5857363/using-multiple-forms-on-a-page-in-django
# Buscar en
#https://www.google.com.mx/search?noj=1&q=django+formview+multiple+forms&revid=538944700&sa=X&ei=XQTCU-zfNuSF8AHLn4GACw&ved=0CIQBENUCKAQ4Cg&biw=1366&bih=657

@login_required
def add(request):
    #import ipdb; ipdb.set_trace()
    usuario  = User.objects.get(username=request.user.username)
    promotor = Promotor.objects.get(usuario=request.user.id)
    
    if request.method=='POST':
        form = EventoForm(request.POST,request.FILES,prefix="sch")
        ubicacion = DestinoForm(request.POST,prefix="loc")
        
        if form.is_valid() and ubicacion.is_valid():
            destino = ubicacion.save()
            evento = form.save(commit = False)
            evento.destino = destino
            evento.Promotor = promotor
            evento.save()
            return HttpResponseRedirect("/miseventos")
        #return HttpResponseForbidden('allowed only via POST')
    else:
        form = EventoForm()
        ubicacion = DestinoForm()
    
    template = "form.html"
    return render_to_response(template,context_instance=RequestContext(request,locals()))

