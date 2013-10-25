from django import template
register = template.Library()

@register.simple_tag
def blog_comments(blog):
    comments = blog.comments.all()
    return comments.count()
