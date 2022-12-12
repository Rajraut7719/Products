from django.shortcuts import render

from .models import productImageModel,productMainModel
from .serializer import productMainModelSerializer
from django.http import Http404
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import generics
from rest_framework import status


# Create your views here.
class productMainModelList(APIView):
    """
    List all productMainModelList,  new productMainModelList.
    """
    def get(self, request, format=None):
        product = productMainModel.objects.all()
        product_id=productMainModel.objects.get(id=1)
        serializer = productMainModelSerializer(product, many=True)
        return Response({'Status':True,'msg':'Successfully','data':serializer.data})



class Product_Id(generics.RetrieveAPIView):
    queryset = productMainModel.objects.all()
    serializer_class = productMainModelSerializer

    def retrieve(self, request, *args, **kwargs):
        instance = self.get_object()
        instance.is_read = True
        instance.save()
        serializer = self.get_serializer(instance)
        return Response({'Status':True,'msg':'Successfully','data':serializer.data})

  
   
   