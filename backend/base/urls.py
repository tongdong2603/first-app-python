from django.urls import path
from . import views

urlpatterns = [
    path('', views.getRoutes, name='routes'),
    path('products/', views.getProducts, name='routes'),
    path('product/<str:pk>', views.getProduct, name='routes')
]