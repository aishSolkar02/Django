from django.db import models
from autoslug import AutoSlugField


#Create Manager

class ProductCustomManager(models.Manager):
    def get_queryset(self):
        return super().get_queryset()
    
    def royalCanin(self):
        return super().get_queryset().filter(product_brand="Royal Canin")
    
    def drools(self):
        return super().get_queryset().filter(product_brand="Drools")
        
# Create your models here.
# step 1: create class which inherits model class from models

# #categary--------------------------------------------------------------------------
class Category(models.Model):
    category_name=models.CharField(max_length=100,null=False)
    category_slug=AutoSlugField(populate_from="category_name",unique=True)

    def __str__(self):
        return self.category_name 
    

    #product---------------------------------------------------------------
class Product(models.Model):
    product_name=models.CharField(max_length=100,null=False)
    product_description=models.TextField(default="Add your discription here")
    product_price=models.PositiveIntegerField(default=0)
    product_image=models.ImageField(upload_to="Products/")#image folder path
    product_brand=models.CharField(max_length=100,default="superpet")
    category=models.ForeignKey(Category,on_delete=models.SET_NULL,null=True)

    #arati=models.Manager()#create a new manager
    customManager=ProductCustomManager()
    
    def __str__(self):
        return self.product_name   



