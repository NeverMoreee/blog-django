from django import template
from django.utils.http import urlquote

import markdown
from django.template.defaultfilters import stringfilter
from django.utils.encoding import force_text
from django.utils.safestring import mark_safe

register = template.Library()

@register.filter

def myurlquote(value):
    return urlquote(value)

@register.filter(is_safe=True)
@stringfilter
def mymarkdown(value):
    return mark_safe(markdown.markdown(value, 
        extensions = ['markdown.extensions.fenced_code', 'markdown.extensions.codehilite'],
        safe_mode = True, enable_attributes=False))
