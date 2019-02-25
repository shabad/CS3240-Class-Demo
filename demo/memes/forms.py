from django import forms
from django.forms import ModelForm
from .models import *

class MemeCreationForm(ModelForm):
    class Meta:
        model = Meme
        fields = ('__all__')

class MemeEditForm(ModelForm):
    class Meta:
        model = Meme
        fields = ('__all__')

    def __init__(self, *args, **kwargs):
        meme_id = kwargs.pop('meme_id')
        super(MemeEditForm, self).__init__(*args, **kwargs)
        meme = Meme.objects.get(id=meme_id)
        initial_fields = ['text', 'image_url']
        for field in initial_fields:
            self.fields[field].initial = getattr(meme, field)
