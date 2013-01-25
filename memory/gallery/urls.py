from django.conf.urls import patterns, url

urlpatterns = patterns('',
    url(r"^/(?P<page>\d{1,2})/(?P<targetGallery>\w{2,10})$", "memory.gallery.views.gallery", name="gallery"),
    url(r"^$", "memory.gallery.views.main", name="main"),
    url(r"^/(?P<page>\d{1,2})$", "memory.gallery.views.page", name="page"),
)
