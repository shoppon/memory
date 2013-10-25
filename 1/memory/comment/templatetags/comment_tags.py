# coding:utf-8
from django import template
from django.contrib.contenttypes.models import ContentType
from memory.comment.forms import TreeCommentForm
from memory.comment.models import TreeComment

register = template.Library()

@register.inclusion_tag('comments.html', takes_context=True)
def comments_for(context, obj=None):
    '''
    context: 上下文
    obj: 被评论的对象，留言页面中的obj为None
    '''
    if not obj is None:
        form = TreeCommentForm(context["request"], obj)
    else:
        form = TreeCommentForm(context["request"])
    try:
        context["posted_comment_form"]
    except KeyError:
        context["posted_comment_form"] = form
    context["unposted_comment_form"] = form
    context["comments_for_object"] = obj
    return context

@register.inclusion_tag('comment.html', takes_context=True)
def comments_thread(context, parent=None):
    comment_for_obj = context["comments_for_object"]
    if comment_for_obj:
        #根据comment_for_obj取出相对应的评论。
        comment_type = ContentType.objects.get_for_model(comment_for_obj)
        comments = TreeComment.objects.filter(content_type__pk=comment_type.id, object_id=comment_for_obj.id)
    else:
        # 留言页面的评论。
        comments = TreeComment.objects.filter(content_type=None)
    context["nodes"] = comments
    return context
