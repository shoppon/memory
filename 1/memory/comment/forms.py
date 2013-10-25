# coding: utf-8
from django import forms
from django.utils.crypto import salted_hmac
from memory.comment.models import TreeComment
from django.utils.translation import ugettext as _
import time

class TreeCommentForm(forms.ModelForm):
    content_type = forms.CharField(widget=forms.HiddenInput, required=False)
    object_pk = forms.CharField(widget=forms.HiddenInput, required=False)
    timestamp = forms.IntegerField(widget=forms.HiddenInput, required=False)
    
    username = forms.CharField(label=_("username"), help_text="必填")
    email = forms.EmailField(label="E-mail", help_text="可选", required=False)
    content = forms.CharField(label=_("comment"), widget=forms.Textarea(), help_text="必填")
    
    class Meta:
        model = TreeComment
        exclude = ("content_type", "object_id", "comment_obj", "parent")
        
    def __init__(self, request=None, target_object=None, data=None, initial=None):
        self.target_object = target_object
        
        if initial is None:
            initial = {}
        
        if not target_object is None:
            initial.update(self.generate_security_data())
        super(TreeCommentForm, self).__init__(data=data, initial=initial)
          
    def generate_security_data(self):
        timestamp = int(time.time())
        security_dict = {
            'content_type'  : str(self.target_object._meta),
            'object_pk'     : str(self.target_object._get_pk_val()),
            'timestamp'     : str(timestamp),
            'security_hash' : self.initial_security_hash(timestamp),
        }
        return security_dict
    
    def initial_security_hash(self, timestamp):
        initial_security_dict = {
            'content_type' : str(self.target_object._meta),
            'object_pk' : str(self.target_object._get_pk_val()),
            'timestamp' : str(timestamp),
          }
        return self.generate_security_hash(**initial_security_dict)
    
    def generate_security_hash(self, content_type, object_pk, timestamp):
        info = (content_type, object_pk, timestamp)
        key_salt = "memory.comment.form.TreeCommentForm"
        value = "-".join(info)
        return salted_hmac(key_salt, value).hexdigest()
