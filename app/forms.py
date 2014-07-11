from django import forms
from django.contrib.auth.forms import  UserCreationForm
from django.forms import ModelForm
from models import *
from django.core.context_processors import csrf
from django.shortcuts import render_to_response

class EventoForm(ModelForm):
    
    class Meta:
        model = Evento
        
class UserForm(UserCreationForm):
	pass
		