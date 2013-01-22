from django.shortcuts import render_to_response
from django.template.context import RequestContext
from memory.gallery.models import Image, Gallery

def gallery(request, gallery_name):
    id = Gallery.objects.filter(name=gallery_name)
    images = Image.objects.filter(gallery_id=id)
    context_instance = RequestContext(request, {"images": images})
    return render_to_response("gallery.html", context_instance)
