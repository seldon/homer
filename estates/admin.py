from django.contrib import admin
from imagekit.admin import AdminThumbnail

from estates.models import EstateImage, Estate, Typology, Owner, Category

class EstateImageInline(admin.TabularInline):
    model = EstateImage   
    sortable_field_name = "position"
    verbose_name= ""
    list_display =('position', 'original', 'show_thumb')
    fields =('admin_thumb','position','original')
    readonly_fields = ('admin_thumb',)


class TypologyAdmin(admin.ModelAdmin):
    list_display = ('typology', 'first_page',)

admin.site.register(Typology, TypologyAdmin)


class OwnerAdmin(admin.ModelAdmin):
    list_display = ('last_name', 'first_name', 'phone', 'email',)

admin.site.register(Owner, OwnerAdmin)


class EstateAdmin(admin.ModelAdmin):
    list_display = ('address', 'typology', 'owner', 'surface', 'price', 'first_page',)
    inlines = [ EstateImageInline, ]


admin.site.register(Estate, EstateAdmin)


class EstateImageAdmin(admin.ModelAdmin):
    list_display = ('estate', 'position', 'original', 'admin_thumbnail',)
    admin_thumbnail = AdminThumbnail(image_field='thumbnail')

admin.site.register(EstateImage, EstateImageAdmin)


class CategoryAdmin(admin.ModelAdmin):
    filter_horizontal = ('typology',)

admin.site.register(Category, CategoryAdmin)
