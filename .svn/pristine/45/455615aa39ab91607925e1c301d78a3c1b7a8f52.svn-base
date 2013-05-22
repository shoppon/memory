# coding:utf-8
from django.core.exceptions import ObjectDoesNotExist
from django.db.models.loading import get_model
from django.shortcuts import redirect
from memory.comment.forms import TreeCommentForm

def comment(request):
    if request.method == 'POST':  # If the form has been submitted...
        post_data = request.POST
        try:
            model = get_model(*post_data.get("content_type", "").split(".", 1))
            if model:
                obj = model.objects.get(id=post_data.get("object_pk", None))
                form = TreeCommentForm(request.POST, obj, post_data)  # A form bound to the POST data
        except (TypeError, ObjectDoesNotExist):
            # 留言页面的评论
            form = TreeCommentForm(request.POST, None, post_data)
        
        if form.is_valid():  # All validation rules pass
            # Process the data in form.cleaned_data
            treecomment = form.save(commit=False)
            if form.target_object:
                # 保存被评论的对象
                treecomment.comment_obj = form.target_object
                treecomment.save()
                return redirect(treecomment.get_absolute_url())
            else:
                treecomment.save()
                return redirect('/about')
