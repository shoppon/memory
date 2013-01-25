from django.shortcuts import render_to_response
from django.template.context import RequestContext
from memory.gallery.models import Image, Gallery

def gallery(request, page, targetGallery):
    if page == None:
        page = 1
    page = int(page)
    start = 4 * (page - 1)
    end = 4 * page
    galleries = Gallery.objects.all()[start: end]
    images = Image.objects.filter(gallery__name=targetGallery)
    return response(request, page, images, galleries)
    

def main(request):
    galleries = Gallery.objects.all()[0: 4]
    images = Image.objects.filter(gallery=galleries[0])
    return response(request, 1, images, galleries)

def page(request, page):
    page = int(page)
    start = 4 * (page - 1)
    end = 4 * page
    galleries = Gallery.objects.all()[start: end]
    images = Image.objects.filter(gallery=galleries[0])
    return response(request, page, images, galleries)

def response(request, page, images, galleries):
    context_instance = RequestContext(request,
                                      {"images": images, "galleries": galleries, "page": page, "prePage": page - 1, "nextPage": page + 1, })
    return render_to_response("gallery.html", context_instance)
