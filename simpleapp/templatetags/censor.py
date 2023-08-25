from django import template
from django.utils.safestring import mark_safe
import re

register = template.Library()

@register.filter
def censor(value):
    unwanted_words = ['', '']
    censored_value = value
    for word in unwanted_words:
        censored_value = re.sub(rf'\b{word}\b', '*' * len(word), censored_value, flags=re.IGNORECASE)
    return mark_safe(censored_value)