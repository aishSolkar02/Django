from django.contrib import admin
from .models import Product


# Register your models here.

# admin.site.register(Product)

class ProductAdmin(admin.ModelAdmin):
    # model=Product
    list_display=['id','product_name','product_price','product_image','product_brand']

admin.site.register(Product,ProductAdmin)

