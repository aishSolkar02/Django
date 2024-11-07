from django.urls import path # import from main urls
from cart import views
urlpatterns = [
    path('',views.show_cart, name='cart'),
    path('add-to-cart/<int:productId>/',views.add_to_cart,name='add-to-cart'),
    path('update-cart/<int:cartitemId>',views.update_cart,name="update-cart"),
    path('delete-cartitem/<int:cartitemId>',views.delete_cartitem,name="delete-cartitem"),
    path('check-out',views.check_out,name="check-out")

]