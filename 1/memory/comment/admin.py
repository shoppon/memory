from django.contrib import admin
from memory.comment import models

class TreeCommentAdmin(admin.ModelAdmin):
    fields = ('username', 'email', 'content', 'parent', 'content_type')
    list_display = ('username', 'email', 'content', 'publish_time', 'comment_obj')

admin.site.register(models.TreeComment, TreeCommentAdmin)
