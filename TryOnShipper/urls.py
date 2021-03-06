from TryOnShipper.views import *
from django.urls import path

urlpatterns = [
    path('', ShipperView.as_view(), name="index_shipper"),
    path('login/', ShipperLogin.as_view(), ),  # Login Form(get)
    path('login/auth/', ShipperLogin.as_view()),  # Login Process(post)
    path('register/', ShipperRegister.as_view(), ),  # Login Form(get)
    path('register/auth/', ShipperRegister.as_view()),  # Login Process(post)
    # path('shipper/', views.ShipperView.as_view(), name="login_shipper"),  # Shipper Registration Form (get)
    # path('shipper/add/', views.ShipperView.as_view(), name="authenticate_shipper"),  # Shipper Registration Process(post)
]
