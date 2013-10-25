from django.conf.urls import patterns, url

urlpatterns = patterns('',
    url(r"^$", "memory.about.views.main", name="main"),
)
