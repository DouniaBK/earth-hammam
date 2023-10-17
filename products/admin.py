from django.contrib import admin
from .models import Item, Category

# Register your models here.


class ItemAdmin(admin.ModelAdmin):
    list_display = ('name', 'category', 'price','sku',)
    list_filter = ("sku", "name", "category", "price",)
    search_fields = ("sku", "name", "category", "price",)
    ordering = ('name',)


class CategoryAdmin(admin.ModelAdmin):
    list_display = ('friendly_name', 'name',)


admin.site.register(Category, CategoryAdmin)
admin.site.register(Item, ItemAdmin)
