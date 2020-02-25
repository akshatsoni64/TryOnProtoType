"""TryOnProtoType URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))`
"""
from django.contrib import admin
from django.urls import path, include
from TryOn import views


urlpatterns = [
    path('',include('TryOn.urls')),
    # path('login/', views.LoginView.as_view()),  # Login Form(get)
    # path('login/auth/', views.LoginView.as_view()),  # Login Process(post)
    #
    # path('customer/', views.CustomerView.as_view()),  # Customer Registration Form (get)
    # path('customer/add/', views.CustomerView.as_view()),  # Customer Registration Process(post)
    #
    # path('vendor/', views.VendorView.as_view()),  # Vendor Registration Form (get)
    # path('vendor/add/', views.VendorView.as_view()),  # Vendor Registration Process(post)
    #
    # path('shipper/', views.ShipperView.as_view()),  # Shipper Registration Form (get)
    # path('shipper/add/', views.ShipperView.as_view()),  # Shipper Registration Process(post)
    #
    # path('vendor/addproducts/', views.ProductUploadView.as_view()),  # Product Upload Module
    # path('vendor/products/', views.ProductDisplayView.as_view()),  # Product Display Module
]
