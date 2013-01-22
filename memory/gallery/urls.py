from django.conf.urls import patterns, url

urlpatterns = patterns('',
    url(r"^(\w{2,10})$", "memory.gallery.views.gallery", name="gallery"),
)
