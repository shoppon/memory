from django.conf.urls import patterns, include, url
from django.contrib import admin
from django.views.generic.simple import direct_to_template

# Uncomment the next two lines to enable the admin:
admin.autodiscover()

urlpatterns = patterns('',
    # Examples:
     url(r'^upload$', 'memory.upload.views.upload', name='upload'),

    # Uncomment the admin/doc line below to enable admin documentation:
    # url(r'^admin/doc/', include('django.contrib.admindocs.urls')),

    # Uncomment the next line to enable the admin:
     url(r'^admin/', include(admin.site.urls)),
     
     url(r'^$', direct_to_template, {"template": "index.html"}, name='home'),
     
     url(r'^gallery', include('memory.gallery.urls')),
     
     url(r'^tweet', include('memory.tweet.urls')),
)
