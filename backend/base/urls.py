from django.urls import path
from . import views

urlpatterns = [
    path('user/login/', views.MyTokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('', views.getRoutes, name='routes'),
    path('user/profile/', views.getUserProfile, name='users'),
    path('products/', views.getProducts, name='routes'),
    path('product/<str:pk>', views.getProduct, name='routes')
]
