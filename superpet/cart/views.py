from django.shortcuts import render,HttpResponseRedirect
from .models import Cart,CartItem
from products.models import Product

# Create your views here.

def add_to_cart(request,productId):
    print("****************",productId,"***************")
    print(request.user)
    currentUser=request.user
    cart,created=Cart.objects.get_or_create(user=currentUser)
    cartitem,created=CartItem.objects.get_or_create(cart=cart,products=Product.customManager.get(id=productId)) #cart from above cart variable
    quantity=int(request.GET.get("quantity"))
    if created:
        cartitem.quantity=quantity
    else:
        cartitem.quantity=cartitem.quantity+quantity
    cartitem.save()

    return HttpResponseRedirect("/products")

def show_cart(request):
    currentUser=request.user
    cart=Cart.objects.get(user=currentUser)
    cartitems=cart.cartitem_set.all()
    total=0
    for cartitem in cartitems:
        total+=cartitem.quantity*cartitem.products.product_price
    return render(request,"cart.html",{"cartitems":cartitems,"total":total})
