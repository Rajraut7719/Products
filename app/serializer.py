from rest_framework import serializers
from .models import productMainModel,productColourModel,productImageModel


class productMainModelSerializer(serializers.ModelSerializer):
    class Meta:
        model = productMainModel
        fields = ['id', 'title', 'description', 'price', 'unique_code', 'Size','quality']