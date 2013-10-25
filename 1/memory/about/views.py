from django.template import RequestContext
from django.template.response import TemplateResponse

def main(request):
    context_instance = RequestContext(request, {
        'is_about': True,
    })
    return TemplateResponse(request, 'about.html', context_instance)