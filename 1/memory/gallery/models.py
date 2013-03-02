from django.db import models

class Gallery(models.Model):
    name = models.CharField(max_length=128)
    cover = models.CharField(max_length=128)
    
    def __unicode__(self):
        return self.name

class Image(models.Model):
    path = models.CharField(max_length=128)
    gallery = models.ForeignKey(Gallery)
