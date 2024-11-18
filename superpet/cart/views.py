from django.shortcuts import render,HttpResponseRedirect
from .models import Cart,CartItem,Order,OrderItem
from products.models import Product
from .forms import OrderForm
import uuid
import razorpay
from django.views.decorators.csrf import csrf_exempt
from django.core.mail import send_mail
from superpet.settings import EMAIL_HOST_USER
from django.contrib.auth.decorators import login_required

# Create your views here.
@login_required(login_url="/login")
def add_to_cart(request,productId):
    print("****************",productId,"***************")
    print(request.user)
    currentUser=request.user
    cart,created=Cart.objects.get_or_create(user=currentUser)
    request.session["cart_id"]=cart.id
    cartitem,created=CartItem.objects.get_or_create(cart=cart,products=Product.customManager.get(id=productId)) #cart from above cart variable
    quantity=int(request.GET.get("quantity"))
    if created:
        cartitem.quantity=quantity
    else:
        cartitem.quantity=cartitem.quantity+quantity
    cartitem.save()

    return HttpResponseRedirect("/products")

# show_cart
@login_required(login_url="/login")
def show_cart(request):
    currentUser=request.user
    cart=Cart.objects.get(user=currentUser)
    cartitems=cart.cartitem_set.all()
    total=0
    for cartitem in cartitems:
        total+=cartitem.quantity*cartitem.products.product_price
    return render(request,"cart.html",{"cartitems":cartitems,"total":total})


# update cart
@login_required(login_url="/login")
def update_cart(request,cartitemId):
    cartitem=CartItem.objects.get(id=cartitemId)
    cartitem.quantity=request.GET.get("quantity")
    cartitem.save()
    return HttpResponseRedirect("/cart")


# delete cart
@login_required(login_url="/login")
def delete_cartitem(request,cartitemId):
    cartitem=CartItem.objects.get(id=cartitemId)
    cartitem.delete()

    return HttpResponseRedirect("/cart")

# check-out
@login_required(login_url="/login")
def check_out(request):
    if request.method=="GET":
        form=OrderForm()
        print(request.session.get("cart_id"))
        return render(request,"checkOut.html",{"form":form})
    if request.method=="POST":
        form=OrderForm(request.POST)
        print(form.is_valid())
        if form.is_valid():
            print(form.cleaned_data)
            order=Order.objects.create(order_id=uuid.uuid4().hex,
                                 user=request.user,
                                 address_line1=form.cleaned_data["address_line1"],
                                 address_line2=form.cleaned_data["address_line2"],
                                 city=form.cleaned_data["city"],
                                 state=form.cleaned_data["state"],
                                 pincode=form.cleaned_data["pincode"],
                                 phone_no=form.cleaned_data["phone_no"])
            cart_id=request.session.get("cart_id")
            cart=Cart.objects.get(id=cart_id)
            cartitems=cart.cartitem_set.all()

            for cartitem in cartitems:
                OrderItem.objects.create(order=order,
                                         quantity=cartitem.quantity,
                                         products=cartitem.products)

           
            
           
    return HttpResponseRedirect("/cart/payment/"+order.order_id)
@login_required(login_url="/login")
def payment(request,orderId):
    order=Order.objects.get(order_id=orderId)
    orderitems=order.orderitem_set.all()       #all method return query set
    total=0
    for orderitem in orderitems:
        total+=orderitem.quantity*orderitem.products.product_price
    client=razorpay.Client(auth=("rzp_test_9OqmIDeq85cvr3","LVkt6Cs9VskcAarHG1ryJNdr"))
    data = { "amount": total*100, "currency": "INR", "receipt":orderId}
    payment = client.order.create(data=data)
    return render(request,"payment.html",{"payment":payment})

@csrf_exempt
@login_required(login_url="/login")
def paymentSuccess(request,orderId):
    razorpay_response={
        "razorpay_payment_id": request.POST.get("razorpay_payment_id"),
        "razorpay_order_id":request.POST.get("razorpay_order_id"),
        "razorpay_signature":request.POST.get("razorpay_signature")
    }
    client = razorpay.Client(auth=("rzp_test_9OqmIDeq85cvr3", "LVkt6Cs9VskcAarHG1ryJNdr"))
    payment_check=client.utility.verify_payment_signature(razorpay_response)
    if  payment_check:
        print("order is paid")
        order=Order.objects.get(order_id=orderId)
        order.paid=True
        order.save()
        send_mail(f"[{order.order_id}placed]",
                  "order placed successfully...",
                  EMAIL_HOST_USER,
                  ["priyanka.vibhute@itvedant.com"],
                  fail_silently=False)
             
    return render (request,"success.html",{"payment_check":payment_check})


    

