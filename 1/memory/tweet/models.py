# -*- coding: utf-8 -*-
from django.contrib.contenttypes import generic
from django.db import models
from django.db.models.fields import DateTimeField
from memory.comment.models import TreeComment

class Tweet(models.Model):
    content = models.TextField(max_length=1024)
    # 发布时间为添加时间
    publish_time = DateTimeField(auto_now_add=True)
    comments = generic.GenericRelation(TreeComment)  
    # 赞数
    like_count = models.IntegerField(default=0)
    
    class Meta:
        ordering = ("-publish_time",)
    
    def __unicode__(self):
        return self.content
