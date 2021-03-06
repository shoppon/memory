from django.contrib import admin
from memory import settings
from memory.gallery import models
from memory.gallery.models import Image
    
class GalleryImageInline(admin.TabularInline):
    model = Image
    extra = 1

class GalleryAdmin(admin.ModelAdmin):
    list_display = ('name', 'cover', 'get_images')
    inlines = (GalleryImageInline, )
    
    class Media:
        js = [settings.TINYMCE_JS, settings.TINYMCE_SETUP_JS, ]
    
class ImageAdmin(admin.ModelAdmin):
    fields = ('gallery', 'path')
    list_display = ('get_gallery_name', 'path')
    
    class Media:
        js = [settings.TINYMCE_JS, settings.TINYMCE_SETUP_JS, ]
    
    def get_gallery_name(self, obj):
        return '%s' % (obj.gallery.name)
    get_gallery_name.short_description = 'Gallery'

admin.site.register(models.Gallery, GalleryAdmin)
admin.site.register(models.Image, ImageAdmin)
