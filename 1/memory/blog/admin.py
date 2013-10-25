from django.contrib import admin
from memory import settings
from memory.blog import models
from memory.blog.models import BlogCategory
from django.utils.translation import ugettext_lazy as _

class BlogCategoryInline(admin.TabularInline):
    model = BlogCategory
    extra = 1
    
class BlogAdmin(admin.ModelAdmin):
    list_display = ('title', 'publish_time', 'update_time')
    inlines = (BlogCategoryInline,)
    
    class Media:
        js = [settings.TINYMCE_JS, settings.TINYMCE_SETUP_JS, ]
        verbose_name = _("blog")
        
class CategoryAdmin(admin.ModelAdmin):
    pass

admin.site.register(models.Blog, BlogAdmin)
admin.site.register(models.Category, CategoryAdmin)
