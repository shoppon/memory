from django.conf.urls import patterns, include, url
from django.contrib import admin
from django.views.generic.base import TemplateView
from filebrowser.sites import site

# Uncomment the next two lines to enable the admin:
admin.autodiscover()

urlpatterns = patterns('',
    # Examples:
     url(r'^upload$', 'memory.upload.views.upload', name='upload'),

    # Uncomment the admin/doc line below to enable admin documentation:
    # url(r'^admin/doc/', include('django.contrib.admindocs.urls')),

    # Uncomment the next line to enable the admin:
     url(r'^admin/', include(admin.site.urls)),
     
     url(r'^$', include('memory.blog.urls')),
     
     url(r'^index$', TemplateView.as_view(template_name="index.html")),
     
     url(r'^blog', include('memory.blog.urls')),
     
     url(r'^gallery', include('memory.gallery.urls')),
     
     url(r'^tweet', include('memory.tweet.urls')),
     
     url(r'^about', include('memory.about.urls')),
     
     url(r'^comment', include('memory.comment.urls')),
     
     url(r'^grappelli/', include('grappelli.urls')),
     
     url(r'^admin/filebrowser/', include(site.urls)),
)
