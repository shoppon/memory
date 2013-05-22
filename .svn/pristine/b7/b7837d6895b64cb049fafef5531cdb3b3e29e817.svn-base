from django.shortcuts import render_to_response
from django.template.context import RequestContext
from memory.blog.models import Blog

def main(request):
    blogs = Blog.objects.all()[0:10]
    context_instance = RequestContext(request, {
        'blogs': blogs,
        'is_blog': True,
    })
    return render_to_response('blog.html', context_instance)

def blog_detail(request, blog_id):
    blog = Blog.objects.get(id=blog_id)
    context_instance = RequestContext(request, {
        'blog': blog,
        'is_blog': True,
    })
    return render_to_response('blog_detail.html', context_instance)
