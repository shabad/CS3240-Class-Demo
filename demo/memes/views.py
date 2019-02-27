from django.shortcuts import render, redirect
from .models import *
from .forms import *

# Create your views here.

def create_meme(request):
    # POST request case
    if request.method == "POST":
        # make a POST request form
        form = MemeCreationForm(request.POST)
        # check to see if form is valid
        if form.is_valid():
            # save the form -- saving the model in the db
            form.save()
            # redirect to a url name
            return redirect('show_all_memes')
    # GET request case -- don't need to specify it in the form parameter
    else:
        form = MemeCreationForm()
    # template to be returned
    link = "memes/create_meme.html"
    # information to be passed to the template
    context = {
        'form':form,
    }
    return render(request, link, context)

def show_all_memes(request):
    # grab all objects of a model
    memes = Meme.objects.all()
    link = "memes/all.html"
    context = {
        'memes':memes,
    }
    return render(request, link, context)

def edit_meme(request, meme_id):
    # grab a specific instance of a model from a unique id
    meme = Meme.objects.get(id=meme_id)
    # POST request case
    if request.method == "POST":
        # make a form object with a POST request and the passed in parameter
        # the parameter is passed just because of how we set up our forms
        # more information available in forms.py
        form = MemeEditForm(request.POST, meme_id=meme_id)
        if form.is_valid():
            # refresh the instance from the databse -- get the most recent values
            meme.refresh_from_db()
            # set all of the fields to the form field
            meme.text = form.cleaned_data.get('text')
            meme.image_url = form.cleaned_data.get('image_url')
            # save the model instance not the form
            # saving the form would create a new object, which we don't want when editing
            meme.save()
            return redirect('show_all_memes')
    else:
        form = MemeEditForm(meme_id=meme_id)
    link = 'memes/edit.html'
    context = {
        'form':form,
    }
    return render(request, link, context)
