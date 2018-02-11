from django.contrib import admin

# Register your models here.

from rango.models import Category, Page


class CategoryAdmin(admin.ModelAdmin):
    list_display = ('name', 'views', 'likes')


class PageAdmin(admin.ModelAdmin):
    list_display = ('title', 'category', 'url', 'views')


admin.site.register(Category, CategoryAdmin)
admin.site.register(Page, PageAdmin)

