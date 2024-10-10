from django.db import models

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


class Product(models.Model):
    product_name=models.CharField(max_length=100,null=False)
    product_description=models.TextField(default="Add your discription here")
    product_price=models.PositiveIntegerField(default=0)
    product_image=models.ImageField(upload_to="Products/")#image folder path
    product_brand=models.CharField(max_length=100,default="superpet")

    #arati=models.Manager()#create a new manager
    customManager=ProductCustomManager()
    
    def __str__(self):
        return self.product_name   


class Categary(models.Model):
    pass
    #categary_type=models.CharField(max_length=100)
    #categary_discription=models.TextField(default="category discription")

