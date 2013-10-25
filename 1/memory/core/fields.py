from django.core.exceptions import ImproperlyConfigured
from django.db import models
from memory import settings
from memory.utils.importing import import_dotted_path

class RichTextField(models.TextField):
    def formfield(self, **kwargs):
        try:
            widget_class = import_dotted_path(settings.RICHTEXT_WIDGET_CLASS)
        except ImportError:
            raise ImproperlyConfigured()
        kwargs["widget"] = widget_class()
        formfield = super(RichTextField, self).formfield(**kwargs)
        return formfield
