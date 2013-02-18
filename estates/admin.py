from estates.models import *
from django.contrib import admin

class TypologyAdmin(admin.ModelAdmin):
    list_display = ('typology', 'first_page')

admin.site.register(Typology, TypologyAdmin)


class CustomerAdmin(admin.ModelAdmin):
    list_display = ('last_name', 'first_name', 'phone', 'email')

admin.site.register(Customer, CustomerAdmin)


class EstateAdmin(admin.ModelAdmin):
    list_display = ('name', 'category', 'surface', 'price', 'customer')

admin.site.register(Estate,EstateAdmin)


admin.site.register(Category)
