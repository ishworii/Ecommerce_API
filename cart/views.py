from rest_framework import generics,permissions
from rest_framework.response import Response
from rest_framework.views import APIView
from cart.models import Cart,CartItem
from cart.serializers import CartSerializer,CartItemSerializer
from products.models import Product
from django.shortcuts import get_object_or_404


class CartDetailView(generics.RetrieveAPIView):
    serializer_class = CartSerializer
    permission_classes = [permissions.IsAuthenticated]

    def get_object(self):
        cart,created = Cart.objects.get_or_create(user=self.request.user)
        return cart
    

class AddtoCartView(APIView):
    permission_classes = [permissions.IsAuthenticated]

    def post(self,request,*args,**kwargs):
        cart,created = Cart.objects.get_or_create(user=request.user)
        product = get_object_or_404(Product,id=request.data.get('product_id'))
        quantity = request.data.get('quantity',1)
        
        cart_item,created = CartItem.objects.get_or_create(cart=cart,product=product)
        if not created:
            cart_item.quantity += int(quantity)
        else:
            cart_item.quantity = int(quantity)
        cart_item.save()

        return Response({'status' : 'success','data' : CartItemSerializer(cart_item).data})

