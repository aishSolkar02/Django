from django.test import TestCase
from .models import Product,Category

# Create your tests here.
def add(a,b):
    return a+b

class ProductTest(TestCase):# data setup for product
    def setUp(self):
        self.product=Product.customManager.create(product_name="test product",
                                     product_description="description for test",
                                     product_price="5000",
                                     product_brand="superpet")
    def test_add(self):
        expectedAnswer=11
        actualAnswer=add(5,6)
        self.assertEqual(expectedAnswer,actualAnswer)


    def test_add_product(self):
        product=Product.customManager.get(id=self.product.id)
        self.assertEqual(self.product,product)

    def test_update_product(self):
        product=Product.customManager.get(id=self.product.id)
        self.assertEqual(self.product,product)


    def test_all_product(self):
        products=Product.customManager.all()
        ans=len(products)>0
        self.assertTrue(ans)
# =====================================================================

class CategoryTest(TestCase):
    def setUp(self):
        self.category=Category.objects.create(category_name="test category",
                                 category_slug="slug")
    
    def test_add(self):
        expectedAnswer=11
        actualAnswer=add(5,6)
        self.assertEqual(expectedAnswer,actualAnswer)

    def test_add_category(self):
        category=Category.objects.get(id=self.category.id)
        self.assertEqual(self.category,category)



    # def test_delete_product(self):
    #     pass

    # def test_all_products(self):
    #     pass

    # def test_update_product(self):
    #     pass
