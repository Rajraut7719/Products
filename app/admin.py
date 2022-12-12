from django.contrib import admin
from .models import productMainModel,productImageModel,productColourModel
# Register your models here.

admin.site.register(productMainModel)
admin.site.register(productImageModel)
admin.site.register(productColourModel)

# admin.site.register(productMainModel)
