from django.shortcuts import render
from .models import Product
from django.contrib.auth.models import User

from rest_framework.views import APIView

from rest_framework.response import Response
from rest_framework import status

from .serializers import productSerializer, UserSerializer


class ProductList(APIView):
    
    def get(self, request):
        products = Product.objects.all()
        serializer = productSerializer(products, many=True)
        return Response(serializer.data)
    
    def post(self, request):
        serializer = productSerializer(data=request.data)
        
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    
class ProductDetail(APIView):
        
        def get_object(self, pk):
            try:
                return Product.objects.get(pk=pk)
            except Product.DoesNotExist:
                return Response(status=status.HTTP_404_NOT_FOUND)
            
        def get(self, request, pk):
            product = self.get_object(pk)
            serializer = productSerializer(product)
            return Response(serializer.data)
        
        def put(self, request, pk):
            product = self.get_object(pk)
            serializer = productSerializer(product, data=request.data)
            
            if serializer.is_valid():
                serializer.save()
                return Response(serializer.data)
            
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
        
        def delete(self, request, pk):
            product = self.get_object(pk)
            product.delete()
            return Response(status=status.HTTP_204_NO_CONTENT)






# Create your views here.
