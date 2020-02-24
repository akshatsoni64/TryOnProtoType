from . import views
from django.urls import path
urlpatterns = [
    path('', views.index,name="index"),
    path('shop/',views.shop,name="shop"),   
    path('feature/',views.features,name="features"),   
    path('contact/',views.contact,name="contact"), 
    path('productdetails/',views.product_details,name="product-details")  
]