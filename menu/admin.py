from django.contrib import admin
from menu.models import Menu, MenuItem

admin.site.register(Menu)


@admin.register(MenuItem)
class MenuItemAdmin(admin.ModelAdmin):
    list_display = ('title', 'parent', 'menu', 'url')
    list_filter = ('menu',)
