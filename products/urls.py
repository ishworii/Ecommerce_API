from django.urls import path
from products import views

urlpatterns = [
    path('', views.ProductList.as_view(), name='product-list'),
    path('<int:pk>/', views.ProductDetail.as_view(), name='product-detail')
]
