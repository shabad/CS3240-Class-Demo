from django.db import models

# Create your models here.

# basic model that has a text field and a url field for images
class Meme(models.Model):
    text = models.CharField(max_length=50)
    image_url = models.URLField(null=True)
