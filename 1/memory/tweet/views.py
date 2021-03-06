from django.shortcuts import render_to_response
from django.template.context import RequestContext
from memory.tweet.models import Tweet

def main(request):
    tweets = Tweet.objects.all()
    context_instance = RequestContext(request, {
        'tweets': tweets,
        'is_tweet': True,
    })
    return render_to_response("tweet.html", context_instance)
