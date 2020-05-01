from django import template

register = template.Library()


@register.filter
def map_by(values, propName):
    """Map list by value"""
    return list(map(lambda x: getattr(x, propName), values))
