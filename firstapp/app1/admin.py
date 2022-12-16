from django.contrib import admin

from .models import Product


class ProductAdmin(admin.ModelAdmin):
    fields = ['name','price','quantity', 'image_url']


admin.site.register(Product)
# Register your models here.