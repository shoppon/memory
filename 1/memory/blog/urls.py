from django.conf.urls import patterns, url

urlpatterns = patterns('',
    url(r"^$", "memory.blog.views.main", name="main"),
    url(r"^/(?P<blog_id>\d{1,5})$", "memory.blog.views.blog_detail", name="blog_detail_id"),
    url(r"^/(?P<blog_id>\d{1,5})#comment(?P<comment_id>\d{1,5})", "memory.blog.views.blog_detail"),
)
