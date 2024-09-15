from django.urls import path
from django.contrib.auth import views as auth_views  # Import auth_views

from core.views import homepage, shop, signup, myAccount, account_edit
from product.views import product
from .views import about  # Import the about view

urlpatterns = [
    path("", homepage, name="homepage"),
    path("signup/", signup, name="signup"),
    path("login/", auth_views.LoginView.as_view(template_name='core/login.html'), name="login"),
    path("myaccount/", myAccount, name="myAccount"),
    path("myaccount/account_edit/", account_edit, name="account_edit"),
    path("logout/", auth_views.LogoutView.as_view(next_page='/'), name="logout"),
    path("shop/", shop, name="shop"),
    path("shop/<slug:slug>/", product, name="product"),
    path("about/", about, name="about"),
]
