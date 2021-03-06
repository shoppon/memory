# coding: utf-8
from django.contrib.contenttypes import generic
from django.db import models
from filebrowser.fields import FileBrowseField
from memory.comment.models import TreeComment

class Gallery(models.Model):
    name = models.CharField(max_length=128)
    cover = FileBrowseField("Image", max_length=200, directory="images/", extensions=[".jpg"], blank=True, null=True)
    # 创建时间
    publish_time = models.DateTimeField(auto_now=True)
    
    def __unicode__(self):
        return self.name
    
    def get_images(self):
        return Image.objects.filter(gallery=self)

class Image(models.Model):
    path = FileBrowseField("Image", max_length=200, directory="images/", extensions=[".jpg"], blank=True, null=True)
    # 创建时间
    publish_time = models.DateTimeField(auto_now=True)
    comments = generic.GenericRelation(TreeComment)
    gallery = models.ForeignKey(Gallery)
    
    def get_thumbnail_url(self):
        thumbnail = self.path.filename_root + "_admin_thumbnail" + self.path.extension
        return self.path.url.replace(self.path.filename, thumbnail)
