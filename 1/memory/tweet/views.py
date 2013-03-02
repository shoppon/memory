from django.shortcuts import render_to_response
from django.template.context import RequestContext
def main(request):
    context_instance = RequestContext(request)
    return render_to_response("tweet.html", context_instance)
