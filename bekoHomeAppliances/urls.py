from django.contrib import admin
from django.urls import path
from django.conf import settings
from django.conf.urls.static import static

from core.views import homepage, shop, signup, login
from product.views import product
from cart.views import add_to_cart

urlpatterns = [
    path("", homepage, name="homepage"),
    path("signup/", signup, name="signup"),
    path("login/", login, name="login"),
    path("shop/", shop, name="shop"),
    path("shop/<slug:slug>/", product, name="product"),
    path('admin/', admin.site.urls),
    path("add_to_cart/<int:product_id>/", add_to_cart, name="add_to_cart")
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)