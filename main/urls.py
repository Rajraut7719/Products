
from django.contrib import admin
from django.urls import path
from app import views
urlpatterns = [
    path('admin/', admin.site.urls),
    path('all_product/',views.productMainModelList.as_view()),
    path('productid/<int:pk>',views.Product_Id.as_view())
]
