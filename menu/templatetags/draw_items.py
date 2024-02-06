from django import template
from ..models import MenuItem

register = template.Library()


@register.inclusion_tag('menu/template_tags/draw_items.html', takes_context=True)
def draw_items(context, title):
    try:
        parent_item = MenuItem.objects.get(title=title)
        items = MenuItem.objects.filter(parent=parent_item, menu=parent_item.menu)
        return {'parent': parent_item, 'items': items, 'context': context}
    except MenuItem.DoesNotExist:
        return {'parent': '', 'items': '', 'context': context}
