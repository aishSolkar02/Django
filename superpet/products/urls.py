from django.urls import path
from . import views

urlpatterns=[
    path('',views.products,name='products'),
    path('royal-Canin/',views.royalCanin,name="royalCanin"),
    path('drools/',views.drools,name="drool")
]