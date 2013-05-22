from django.contrib import admin
from memory import settings
from memory.blog import models

class BlogAdmin(admin.ModelAdmin):
    fields = ('title', 'content')
    list_display = ('title', 'publish_time', 'update_time')
    
    class Media:
        js = [settings.TINYMCE_JS, settings.TINYMCE_SETUP_JS, ]

admin.site.register(models.Blog, BlogAdmin)
