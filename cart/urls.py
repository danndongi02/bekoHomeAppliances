from django.urls import path, include

from django.urls import path, include

from cart.views import (
    add_to_cart, 
    cart, 
    checkout, 
    update_cart, 
    hx_menu_cart, 
    hx_cart_total,
    remove_from_cart,  # Import the new view
)

urlpatterns = [
    path("", cart, name="cart"),
    path("checkout/", checkout, name="checkout"),
    path("add_to_cart/<int:product_id>/", add_to_cart, name="add_to_cart"),
    path("update_cart/<int:product_id>/<str:action>/", update_cart, name="update_cart"),
    path("hx_menu_cart/", hx_menu_cart, name="hx_menu_cart"),
    path("hx_cart_total/", hx_cart_total, name="hx_cart_total"),
    path('remove_from_cart/<int:product_id>/', remove_from_cart, name='remove_from_cart'),
]
