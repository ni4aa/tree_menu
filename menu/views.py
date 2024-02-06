from django.shortcuts import render
from django.views.generic.base import TemplateView
from menu.models import Menu, MenuItem


class IndexView(TemplateView):
    template_name = 'menu/index.html'

    def get_context_data(self, **kwargs):
        context = super(IndexView, self).get_context_data()
        context['title'] = 'Menu'
        menu = Menu.objects.get(title='First menu')
        context['items'] = MenuItem.objects.filter(menu=menu)
        return context
