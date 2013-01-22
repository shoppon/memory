from _pyio import open
from django.http import HttpResponse
from django.views.decorators.csrf import csrf_exempt

@csrf_exempt
def upload(request):
    if request.method == 'POST':
        imagePath = '/m.jpg'
        destination = open(imagePath, 'wb+')
        print request.FILES['file_path']
        for chunk in request.FILES['file_path'].chunks():
            destination.write(chunk)
        destination.close()
        return HttpResponse("hello world")
    return HttpResponse("get")
