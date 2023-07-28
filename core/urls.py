from django.urls import path
from django.contrib.auth import views

from core.views import homepage, shop, signup, user_login
from product.views import product

urlpatterns = [
    path("", homepage, name="homepage"),
    path("signup/", signup, name="signup"),
    path("login/", views.LoginView.as_view(template_name='core/login.html'), name="login"),
    path("logout/", views.LogoutView.as_view(), name="logout"),
    path("shop/", shop, name="shop"),
    path("shop/<slug:slug>/", product, name="product"),
]
