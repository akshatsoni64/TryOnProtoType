from TryOnVendor import views
from TryOnShipper import views
from TryOn import views
from django.urls import path
urlpatterns = [
    path('', views.index,name="index"),
    path('shop/',views.shop,name="shop"),
    path('feature/',views.features,name="features"),
    path('contact/',views.contact,name="contact"),
    path('productdetails/',views.product_details,name="product-details"),
    path('logout/', views.logout,name="logout"),
    # path('register/', views.register,name="register"),
    path('login/', views.LoginView.as_view(),name="login"),
    path('register/', views.RegisterView.as_view(), name="register_customer"),  # Customer Registration Form (get)
    path('register/auth/', views.RegisterView.as_view(), name="authenticate_customer"),  # Customer Registration Process(post)
]