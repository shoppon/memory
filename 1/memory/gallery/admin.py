from django import forms
from django.conf.urls import patterns
from django.contrib import admin
from memory.gallery import models
from memory.upload.views import upload

class GalleryAdmin(admin.ModelAdmin):
    list_display = ('name', 'cover')
    
class ImageModelForm(forms.ModelForm):
    path = forms.ImageField(required=True)

class ImageAdmin(admin.ModelAdmin):
    form = ImageModelForm
    list_display = ('get_gallery_name', 'path')
    
    def get_gallery_name(self, obj):
        return '%s' % (obj.gallery.name)
    get_gallery_name.short_description = 'Gallery'
    
    def get_urls(self):
        urls = super(ImageAdmin, self).get_urls()
        my_urls = patterns('',
            (r'^upload/$', upload)
        )
        return my_urls + urls
    
admin.site.register(models.Gallery, GalleryAdmin)
admin.site.register(models.Image, ImageAdmin)
