from django.shortcuts import render, redirect
from .models import *
from .forms import *

# Create your views here.

def create_meme(request):
    if request.method == "POST":
        form = MemeCreationForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('show_all_memes')
    else:
        form = MemeCreationForm()
    link = "memes/create_meme.html"
    context = {
        'form':form,
    }
    return render(request, link, context)

def show_all_memes(request):
    memes = Meme.objects.all()
    link = "memes/all.html"
    context = {
        'memes':memes,
    }
    return render(request, link, context)

def edit_meme(request, meme_id):
    meme = Meme.objects.get(id=meme_id)

    if request.method == "POST":
        form = MemeEditForm(request.POST, meme_id=meme_id)
        if form.is_valid():
            meme.refresh_from_db()
            meme.text = form.cleaned_data.get('text')
            meme.image_url = form.cleaned_data.get('image_url')
            meme.save()
            return redirect('show_all_memes')
    else:
        form = MemeEditForm(meme_id=meme_id)
    link = 'memes/edit.html'
    context = {
        'form':form,
    }
    return render(request, link, context)
