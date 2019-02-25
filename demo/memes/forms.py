from django import forms
from django.forms import ModelForm
from .models import *

class MemeCreationForm(ModelForm):
    class Meta:
        model = Meme
        fields = ('__all__')
        
