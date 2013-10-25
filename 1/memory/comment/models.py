# coding: utf-8
from django.contrib.contenttypes import generic
from django.contrib.contenttypes.models import ContentType
from django.db import models
from django.db.models.fields import DateTimeField
from mptt.fields import TreeForeignKey
from django.utils.translation import ugettext_lazy as _
from mptt.models import MPTTModel

class TreeComment(MPTTModel):
    username = models.CharField(max_length=128)
    email = models.EmailField()
    content = models.TextField()
    parent = TreeForeignKey('self', null=True, blank=True, related_name='child')
    # 发布时间为添加时间
    publish_time = DateTimeField(auto_now_add=True, verbose_name=_("publish_time"))
    
    # contenttypes
    content_type = models.ForeignKey(ContentType, null=True, blank=True)
    object_id = models.PositiveIntegerField(null=True, blank=True)
    comment_obj = generic.GenericForeignKey('content_type', 'object_id')
    
    class Meta:
        verbose_name = _("comment")
        ordering = ("-publish_time",)
    
    def __unicode__(self):
        return self.content
    
    def get_absolute_url(self):
        url = self.comment_obj.get_absolute_url()
        return "%s#comment-%s" % (url, self.id)
