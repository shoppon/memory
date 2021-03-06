from django.contrib import admin
from memory.tweet import models

class TweetAdmin(admin.ModelAdmin):
    fields = ('content',)
    list_display = ('content', 'like_count', 'publish_time')

admin.site.register(models.Tweet, TweetAdmin)
