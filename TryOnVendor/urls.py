from TryOnVendor.views import *
from django.urls import path

urlpatterns = [
    path('', VendorView.as_view(), name="index_vendor"),
    path('register/', VendorRegister.as_view(), name="login_vendor"),  # Login Form(get)
    path('register/auth/', VendorRegister.as_view(), name="authenticate"),  # Login Process(post)
    path('login/', VendorLogin.as_view(), name="login_vendor"),  # Login Form(get)
    path('login/auth/', VendorLogin.as_view(), name="authenticate"),  # Login Process(post)
    # path('vendor/', views.VendorView.as_view(), name="index"),  # Vendor Registration Form (get)
    # path('vendor/add/', views.VendorView.as_view(), name="index"),  # Vendor Registration Process(post)
    # path('vendor/addproducts/', views.ProductUploadView.as_view(), name="index"),  # Product Upload Module
    # path('vendor/products/', views.ProductDisplayView.as_view(), name="index"),  # Product Display Module
]
