from django import forms
from django.forms import ModelForm
from .models import *

# ModelForm for Meme creation
class MemeCreationForm(ModelForm):
    # specify model for the ModelForm to be based off of
    class Meta:
        model = Meme
        # specify fields to be displayed
        fields = ('__all__')

# ModelForm for Meme Editing
class MemeEditForm(ModelForm):
    # specify model for the ModelForm to be based off of
    class Meta:
        model = Meme
        # specify fields to be displayed
        fields = ('__all__')

    # setting all of the form fields initial values
    def __init__(self, *args, **kwargs):
        # this is a parameter we passed to the form in views.py
        meme_id = kwargs.pop('meme_id')
        super(MemeEditForm, self).__init__(*args, **kwargs)
        # grab the meme object based on the passed id
        meme = Meme.objects.get(id=meme_id)
        # these are the fields (all of them), that we want to set initial values for
        initial_fields = ['text', 'image_url']
        for field in initial_fields:
            # set the initial value
            self.fields[field].initial = getattr(meme, field)
