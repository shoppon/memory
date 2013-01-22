from django.db import models

class Gallery(models.Model):
    name = models.CharField(max_length=128)

class Image(models.Model):
    path = models.CharField(max_length=128)
    gallery = models.ForeignKey(Gallery)
