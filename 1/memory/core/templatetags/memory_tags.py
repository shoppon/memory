from django import template

register = template.Library()

@register.inclusion_tag("includes/form_fields.html", takes_context=True)
def fields_for(context, form):
    context["form_for_fields"] = form
    return context
