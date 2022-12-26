from django import template
from NewsPortal.models import Post

register = template.Library()

@register.filter()
def censor(value):
    text = value.split()
    text_b = ['***' if word == word.upper() else word for word in text]
    return ' '.join(text_b)
