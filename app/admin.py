from django.contrib import admin
from .models import *
# Register your models here.
@admin.register(Product)
class ProductModelAdmin(admin.ModelAdmin):
    list_display = ['id', 'title', 'discounted_price', 'category', 'product_image']

@admin.register(CustomUser)
class CustomerModelAdim(admin.ModelAdmin):
    list_display = ['id', 'username','email', 'locality', 'mobile', 'city', 'zipcode']


@admin.register(Cart)
class CartModelAdmin(admin.ModelAdmin):
    list_display = ['id', 'user', 'product', 'quantity']