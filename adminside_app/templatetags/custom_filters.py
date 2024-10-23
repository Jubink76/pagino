from django import template

register = template.Library()

@register.filter(name='add_class')
def add_class(field, css_class):
    """Adds a CSS class to a form field."""
    if hasattr(field, 'widget'):
        return field.widget(attrs={'class': css_class})
    return field

