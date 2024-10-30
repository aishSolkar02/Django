from django.urls import path # import from mean urls
from cart import views
urlpatterns = [
    path('',views.show_cart, name='cart'),
    path('add-to-cart/<int:productId>/',views.add_to_cart,name='add-to-cart')
]