# -*- coding: utf-8 -*-
from django.contrib.contenttypes import generic
from django.core.urlresolvers import reverse
from django.db import models
from django.db.models.fields import CharField, DateTimeField
from django.forms.fields import URLField
from django.utils.translation import ugettext_lazy as _
from memory.comment.models import TreeComment
from memory.core.fields import RichTextField
import re

class Category(models.Model):
    name = CharField(max_length=32)
    # 每个分类可以有多个子分类
    parent_category = models.ForeignKey('self', null=True, blank=True)
    
    def __unicode__(self):
        return self.name
    
    class Meta:
        verbose_name = _("category")

class Blog(models.Model):
    title = CharField(verbose_name=_("title"), max_length=1024)
    # 内容
    content = RichTextField(verbose_name=_("content"))
    url = URLField()
    # 发布时间为添加时间
    publish_time = DateTimeField(auto_now_add=True, verbose_name=_("publish_time"))
    # 修改时间自动为保存的时间
    update_time = DateTimeField(auto_now=True, verbose_name=_("update_time"))
    # 使用GenericRelation， 一定要指定object_id_field
    comments = generic.GenericRelation(TreeComment, verbose_name=_("comments"))
    # 博客和分类是多对多关系
    categorys = models.ManyToManyField(Category, through='BlogCategory')
    
    class Meta:
        verbose_name = _("blog")
        ordering = ("-publish_time",)
    
    def __unicode__(self):
        return self.title
    
    def get_absolute_url(self):
        return reverse('memory.blog.views.blog_detail', args=[str(self.id)])
     
    # 提取博客摘要   
    def summary(self):
        content = self.content
        maxlen = 200  # 显示字数
        showimg = ''  # 空　表示不显示图片 img 显示图片
        # 过虑段落标记
        content = re.sub('</?(P|p)[^<>]*/?>', '', content)
        # 过虑图片标记
        if showimg != 'img':
            content = re.sub('</?(IMG|img)[^<>]*/?>', '', content)
    
        n = 0
        result = ''
        temp = ''
        isCode = False  # 是不是HTML代码
        isHtml = False  # 是不是HTML特殊字符,如&nbsp;
        # 获取指定长度的内容
        for i in range(len(content)):
            temp = content[i]
            if temp == '<':
                isCode = True
            elif temp == '&':
                isHtml = True
            elif temp == '>' and isCode:
                n = n - 1
                isCode = False
            elif temp == ';' and isHtml:
                isHtml = False
            if not isCode and not isHtml:
                n = n + 1
            result += temp
            if n >= maxlen:
                break
        
        # 取出所有html标记
        temp_result = re.sub('(>)[^<>]*(<?)', '><', result)
        temp_result = temp_result.lower()
        if len(content) - len(temp_result) < maxlen:
            return content
        
        # 去掉不需要结束标记html标记
        rg = ("</?(AREA|BASE|BASEFONT|BODY|BR|COL|COLGROUP|DD|DT|FRAME|HEAD|"
            "HR|HTML|IMG|INPUT|ISINDEX|LI|LINK|META|OPTION|P|PARAM|TBODY|TD|"
            "TFOOT|TH|THEAD|TR|area|base|basefont|body|br|col|colgroup|dd|dt|"
            "frame|head|hr|html|img|input|isindex|li|link|meta|option|p|param|"
            "tbody|td|tfoot|th|thead|tr)[^<>]*/?>")
        temp_result = re.sub(rg, '', temp_result)
        # 去掉成对的html标记
        temp_result = re.sub('<([a-zA-Z]+)[^<>]*>(.*?)</\\1>', '', temp_result)
        # 取出html标记符号
        arr = re.findall('<([a-zA-Z]+)[^<>]*>', temp_result)
        # 补全html标记
        for i in range(len(arr)):
            result += '</%s>' % arr[len(arr) - i - 1]
        return result

class BlogCategory(models.Model):
    blog = models.ForeignKey(Blog)
    category = models.ForeignKey(Category)
