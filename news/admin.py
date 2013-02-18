from news.models import News
from django.contrib import admin

class NewsAdmin(admin.ModelAdmin):
    list_display = ('title', 'date', 'user')    

admin.site.register(News, NewsAdmin)

