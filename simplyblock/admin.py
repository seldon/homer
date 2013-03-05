from simplyblock.models import *
from django.contrib import admin

class ContentAdmin(admin.ModelAdmin):
    list_display = ('title', 'block_name','body')

admin.site.register(Content, ContentAdmin)