from django.views.generic import TemplateView,FormView
from django.shortcuts import render_to_response,get_object_or_404
from django.template.context import RequestContext
from forms import * 
from django.http import HttpResponse,HttpResponseRedirect, HttpResponseForbidden
from django.contrib.auth.decorators import login_required
from models import * 
from .forms import UserForm



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
    usuario = User.objects.get(username=request.user.username)
    template = "micuenta.html"
    return render_to_response(template,locals())

@login_required
def miseventos(request):
    evento = Evento.objects.all()
    template = "miseventos.html"
    return render_to_response(template,locals())

@login_required
def add(request):
    if request.method =="POST":
        form = EventoForm(request.POST,request.FILES)
        if form.is_valid():
            evento = form.save(commit = False)
            evento.save()
            return HttpResponseRedirect("/")
        #return HttpResponseForbidden('allowed only via POST')
    else:
        form = EventoForm()
    
    template = "form.html"
    return render_to_response(template,context_instance=RequestContext(request,locals()))

