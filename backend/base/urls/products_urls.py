from django.urls import path
from ..views import products_views as views

urlpatterns = [

    path('', views.getProducts, name='routes'),
    path('<str:pk>', views.getProduct, name='routes')
]
