from django import template

register = template.Library()


@register.filter()
def cut_string(text, length):
    return text[:length]
