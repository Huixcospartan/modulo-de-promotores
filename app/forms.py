from django import forms
from django.contrib.auth.forms import  UserCreationForm
from django.forms import ModelForm
from models import *
from django.core.context_processors import csrf
from django.shortcuts import render_to_response

class EventoForm(ModelForm):
    
    class Meta:
        model = Evento
        exclude = ('Promotor','destino',)

class DestinoForm(ModelForm):
    class Meta:
        model = Destino

#from django.contrib.auth.models import User        
class UserForm(UserCreationForm):
	nombre 		= forms.CharField(max_length = 45)
	paterno	 	= forms.CharField(max_length = 45)
	materno 	= forms.CharField(max_length = 45)

	#class Meta:
	#	model = User	