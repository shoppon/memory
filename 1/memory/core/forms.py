from django import forms
from memory import settings

class TinyMceWidget(forms.Textarea):

    class Media:
        js = settings.TINYMCE_JS

    def __init__(self, *args, **kwargs):
        super(TinyMceWidget, self).__init__(*args, **kwargs)
        self.attrs["class"] = "mceEditor"
