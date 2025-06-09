from django import template
import markdown
from django.utils.safestring import mark_safe

register = template.Library()

@register.filter(name='markdown')
def markdown_filter(text):
    if not text:
        return ""
    return mark_safe(markdown.markdown(text, extensions=['extra', 'codehilite'])) 