from django.urls import path
from cart.views import CartDetailView,AddtoCartView


urlpatterns = [
    path('cart/',CartDetailView.as_view(),name='cart-detail'),
    path('cart/add/',AddtoCartView.as_view(),name='add-to-cart'),
]
