from django.contrib import admin
from memory import settings
from memory.blog import models
from memory.blog.models import BlogCategory

class BlogCategoryInline(admin.TabularInline):
    model = BlogCategory
    extra = 1
    
class BlogAdmin(admin.ModelAdmin):
    list_display = ('title', 'publish_time', 'update_time')
    inlines = (BlogCategoryInline,)
    
    class Media:
        js = [settings.TINYMCE_JS, settings.TINYMCE_SETUP_JS, ]
        
class CategoryAdmin(admin.ModelAdmin):
    pass

admin.site.register(models.Blog, BlogAdmin)
admin.site.register(models.Category, CategoryAdmin)
