from estates.models import *
from django.contrib import admin

class TypologyAdmin(admin.ModelAdmin):
    list_display = ('typology', 'first_page')

admin.site.register(Typology, TypologyAdmin)


class OwnerAdmin(admin.ModelAdmin):
    list_display = ('last_name', 'first_name', 'phone', 'email')

admin.site.register(Owner, OwnerAdmin)


class EstateAdmin(admin.ModelAdmin):
    list_display = ('typology', 'surface', 'price', 'owner', 'first_page')

admin.site.register(Estate,EstateAdmin)

class CategoryAdmin(admin.ModelAdmin):
    filter_horizontal = ('typology',)

admin.site.register(Category, CategoryAdmin)
