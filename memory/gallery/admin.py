from django.contrib import admin
from memory.gallery import models

class GalleryAdmin(admin.ModelAdmin):
    list_display = ('name', 'cover')

class ImageAdmin(admin.ModelAdmin):
    list_display = ('get_gallery_name', 'path')
    
    def get_gallery_name(self, obj):
        return '%s'%(obj.gallery.name)
    get_gallery_name.short_description = 'Gallery'

admin.site.register(models.Gallery, GalleryAdmin)
admin.site.register(models.Image, ImageAdmin)