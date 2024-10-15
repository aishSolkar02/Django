from django.shortcuts import render
from .models import Product
from django.views.generic import ListView,DetailView

# Create your views here.

def products(request):
    return render(request,"products.html")

def royalCanin(request):
    products=Product.customManager.royalCanin()

    return render(request,"products.html",{"products":products})

def drools(request):
    products=Product.customManager.drools()
    return render(request,"products.html",{"products":products})

def search(request):
    keyword=request.GET.get("keyword")
    products=Product.customManager.all().filter(product_name__icontains=keyword)
    return render(request,"products.html",{"products":products})

class ProductListView(ListView):
    model=Product

class ProductDetailView(DetailView):
    model=Product
    template_name="products/productdetail.html"



