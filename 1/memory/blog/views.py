from django.shortcuts import render_to_response
from django.template.context import RequestContext
from memory.blog.models import Blog, Category
from memory.comment.models import TreeComment

def main(request):
    category = request.GET.get('cat')
    if category:
        blogs = Blog.objects.filter(blogcategory__category=category)
    else:
        blogs = Blog.objects.all()[0:10]
    categories = Category.objects.all()
    comments = TreeComment.objects.filter()[0:5]
    context_instance = RequestContext(request, {
        'blogs': blogs,
        'is_blog': True,
        'categories': categories,
        'comments': comments,
    })
    return render_to_response('blog.html', context_instance)

def blog_detail(request, blog_id):
    blog = Blog.objects.get(id=blog_id)
    context_instance = RequestContext(request, {
        'blog': blog,
        'is_blog': True,
    })
    return render_to_response('blog_detail.html', context_instance)

def ajax_get_blogs_by_category(request, category_id):
    blogs = Blog.objects.filter()[0:1]
    categories = Category.objects.all()
    comments = TreeComment.objects.filter()[0:5]
    context_instance = RequestContext(request, {
        'blogs': blogs,
        'is_blog': True,
        'categories': categories,
        'comments': comments,
    })
    return render_to_response('blog.html', context_instance)
