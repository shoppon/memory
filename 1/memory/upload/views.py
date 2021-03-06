from _pyio import open
from django.http import HttpResponse
from django.views.decorators.csrf import csrf_exempt
from memory.gallery.models import Gallery
from memory.settings import MEDIA_ROOT
import os
import uuid

@csrf_exempt
def upload(request):
    if request.method == 'POST':
        # save the file
        galleryName = request.REQUEST['gallery_name']
        gallery = Gallery.objects.get(name=galleryName)
        fileName = request.FILES['file_path'].name
        save(request.FILES['file_path'], gallery, fileName)
        return HttpResponse("upload success")
    return HttpResponse("get")

def save(path, gallery, fileName):
    imageName = str(uuid.uuid4()) + fileName[fileName.rfind("."):]
    imagePath = MEDIA_ROOT + os.sep + imageName
    destination = open(imagePath, 'wb+')
    for chunk in path.chunks():
        destination.write(chunk)
    destination.close()
        
    image = gallery.image_set.create()
    image.path = imageName
    image.save()
