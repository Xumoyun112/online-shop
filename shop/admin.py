from django.contrib import admin
from . import models

admin.site.register(models.Category)
admin.site.register(models.Product)


class CategoryAdmin(admin.ModelAdmin):
    list_display = ('name', 'slug')
    search_fields = ('name')


class ProductAdmin(admin.ModelAdmin):
    list_display = ('name', 'price', 'slug', 'category')
    search_fields = ('name', 'category')
    readonly_fields = ('views')

