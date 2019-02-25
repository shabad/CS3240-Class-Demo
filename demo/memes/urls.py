from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'^create/', views.create_meme, name='create_meme'),
    url(r'^all/', views.show_all_memes, name='show_all_memes'),
]
