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
        albumName = request.REQUEST['album_name']
        fileName = request.FILES['file_path'].name
        imageName = str(uuid.uuid4()) + fileName[fileName.rfind("."):]
        imagePath = MEDIA_ROOT + os.sep + imageName
        destination = open(imagePath, 'wb+')
        for chunk in request.FILES['file_path'].chunks():
            destination.write(chunk)
        destination.close()
        
        # update the database
        gallery = Gallery.objects.get(name=albumName)
        if not gallery:
            gallery = Gallery()
            gallery.name = albumName
            gallery.cover = imageName
            gallery.save()
            
        image = gallery.image_set.create()
        image.path = imageName
        image.save()
      
        return HttpResponse("upload success")
    return HttpResponse("get")
