from django.views.generic import TemplateView,FormView
from django.shortcuts import render_to_response,get_object_or_404, render 
from django.template.context import RequestContext
from forms import * 
from django.views.generic.detail import DetailView
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
def micuenta(request):
    #import ipdb; ipdb.set_trace()
    usuario  = User.objects.get(username=request.user.username)
    promotor = Promotor.objects.get(usuario=request.user.id)
    template = "micuenta.html"
    return render_to_response(template,locals())

@login_required
def editar_micuenta(request):
    #import ipdb; ipdb.set_trace()
    usuario  = User.objects.get(username=request.user.username)
    promotor = Promotor.objects.get(usuario=usuario)
    form = UserForm(request.POST, instance=usuario)
    if form.is_valid():
        form.save(commit=False)
        promotor.nombre     = form.cleaned_data['nombre']
        promotor.paterno    = form.cleaned_data['paterno']
        promotor.materno    = form.cleaned_data['materno']
        form.save()
        promotor.save()
        return HttpResponseRedirect("/micuenta")   
    else:
        form = UserForm()

    template = "editarcuenta.html"
    return render_to_response(template,context_instance=RequestContext(request,locals()))


@login_required
def miseventos(request):
    #import ipdb; ipdb.set_trace()
    promotor = Promotor.objects.get(usuario=request.user.id)
    evento   = Evento.objects.filter(Promotor=promotor)
    template = "miseventos.html"
    return render_to_response(template,locals())

class EventosDetallesView(DetailView):
    model = Evento
    context_object_name = 'evento'
    
    def get_template_names(self):
        return 'detallesevento.html'

@login_required
def evento(request):    
    #import ipdb; ipdb.set_trace()
    promotor = Promotor.objects.get(usuario=request.user.id)
    evento   = Evento.objects.filter(Promotor=promotor)
    template = "eventos.html"
    return render_to_response(template,locals())

@login_required
def eliminar_evento(request,pk):    
    #import ipdb; ipdb.set_trace()
    evento = get_object_or_404(Evento,pk=pk)
    if request.method=='GET':
        evento.delete()
        return HttpResponseRedirect('/miseventos')
    template = "detallesevento.html"
    return render_to_response(template,context_instance=RequestContext(request,locals()))

@login_required
def actualizar_evento(request,pk):
    #import ipdb; ipdb.set_trace()
    usuario  = User.objects.get(username=request.user.username)
    promotor = Promotor.objects.get(usuario=request.user.id)
    evento      = get_object_or_404(Evento,pk=pk)
    formulario  = EventoForm(request.POST,request.FILES, instance=evento)
        
    if formulario.is_valid():
        evento = formulario.save(commit = False)
        evento.Promotor = promotor
        evento.save()
        return HttpResponseRedirect("/miseventos")   
    else:
        formulario = EventoForm()

    template = "editarevento.html"
    return render_to_response(template,context_instance=RequestContext(request,locals()))


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





# http://blog.byjakt.com/multiple-django-forms-in-one-form.html
# http://stackoverflow.com/questions/5857363/using-multiple-forms-on-a-page-in-django
# Buscar en
#https://www.google.com.mx/search?noj=1&q=django+formview+multiple+forms&revid=538944700&sa=X&ei=XQTCU-zfNuSF8AHLn4GACw&ved=0CIQBENUCKAQ4Cg&biw=1366&bih=657
