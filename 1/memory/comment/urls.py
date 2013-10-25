from django.conf.urls import patterns, url

urlpatterns = patterns('',
    url(r"^$", "memory.comment.views.comment"),
)
