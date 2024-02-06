from django import template
from ..models import Menu, MenuItem

register = template.Library()


@register.inclusion_tag('menu/template_tags/draw_menu.html', takes_context=True)
def draw_menu(context, title):
    try:
        menu = Menu.objects.get(title=title)
        items = MenuItem.objects.filter(menu=menu, parent=None)
        return {'menu': menu, 'items': items, 'context': context}
    except Menu.DoesNotExist:
        return {'menu': '', 'items': '', 'context': context}


