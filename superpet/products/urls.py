from django.urls import path
from . import views

urlpatterns=[
    path('',views.ProductListView.as_view(),name='products'),
    path('royal-Canin/',views.royalCanin,name="royalCanin"),
    path('drools/',views.drools,name="drool"),
    path('search/',views.search,name="search"),
    path('<int:pk>/',views.ProductDetailView.as_view(),name="product-detail")

]