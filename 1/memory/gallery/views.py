# -*- coding: utf-8 -*-
from django.shortcuts import render_to_response
from django.template.context import RequestContext
from memory.gallery.models import Image, Gallery

"""
请求指定相册的指定页数
page: 页数
targetGallery: 目标相册
"""
def gallery(request, page, targetGallery):
    if page == None:
        page = 1
    page = int(page)
    start = 4 * (page - 1)
    end = 4 * page
    galleries = Gallery.objects.all()[start: end]
    images = Image.objects.filter(gallery__name=targetGallery)
    return response(request, page, images, galleries)

"""
相册默认页面
"""   
def main(request):
    galleries = Gallery.objects.all()[0: 4]
    if not galleries.count() == 0:
        images = Image.objects.filter(gallery=galleries[0])
    else:
        images = None
    return response(request, 1, images, galleries)

"""
默认相册翻页
"""
def page(request, page):
    page = int(page)
    start = 4 * (page - 1)
    end = 4 * page
    galleries = Gallery.objects.all()[start: end]
    images = Image.objects.filter(gallery=galleries[0])
    return response(request, page, images, galleries)

"""
images:
galleries:
"""
def response(request, page, images, galleries):
    context_instance = RequestContext(request, {
        'images': images,
        'galleries': galleries,
        'page': page,
        'prePage': page - 1,
        'nextPage': page + 1,
        'is_gallery': True,
        'nodes': None,
    })
    return render_to_response("gallery.html", context_instance)
