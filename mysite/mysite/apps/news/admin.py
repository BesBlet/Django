from django.contrib import admin

from .models import News

@admin.register(News)
class NewsAdmin(admin.ModelAdmin):
	list_display = ('news_title', 'news_text')
# Register your models here.
