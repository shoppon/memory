from django.http import HttpResponse, Http404
from django.views.decorators.csrf import csrf_exempt
from django.contrib import auth

@csrf_exempt
def login(request):
    if request.method != 'POST':
        raise Http404('Only POSTs are allowed')
    user = auth.authenticate(username='', password='')
    if user is not None:
        print "Correct"
    else:
        print "Invalid"
    return HttpResponse("login")
