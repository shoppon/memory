from django import template
register = template.Library()

@register.simple_tag
def tweet_comments(tweet):
    comments = tweet.comments.all()
    return comments.count()

@register.simple_tag
def tweet_likes(tweet):
    comments = tweet.comments.all()
    return comments.count()
