from django.template.context import RequestContext
from django.template.response import TemplateResponse

def render(request, templates, dictionary=None, context_instance=None,
           **kwargs):
    dictionary = dictionary or {}
    if context_instance:
        context_instance.update(dictionary)
    else:
        context_instance = RequestContext(request, dictionary)
    return TemplateResponse(request, templates, context_instance, **kwargs)
