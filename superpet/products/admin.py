from django.contrib import admin
from .models import Product,Category


# Register your models here.

# admin.site.register(Product)

class ProductAdmin(admin.ModelAdmin):
    # model=Product
    list_display=['id','product_name','product_price','product_image','product_brand']

class CategoryAdmin(admin.ModelAdmin):
    list_display=['id','category_name','category_slug']

admin.site.register(Product,ProductAdmin)
admin.site.register(Category,CategoryAdmin)


