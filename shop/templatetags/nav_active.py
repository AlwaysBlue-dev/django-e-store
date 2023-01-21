from django import template

register = template.Library()

# Use the active class in current page 
@register.simple_tag
def nav_active(request, link):
    if request.path == link:
        return "active"
    return ""
