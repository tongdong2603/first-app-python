from django.urls import path
from . import views

urlpatterns = [
    path('', views.getRoutes, name='routes'),

    path('user/profile/', views.getUserProfile, name='users'),
    path('user/', views.getUsers, name='users'),
    path('user/login/', views.MyTokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('users/register/', views.registerUser, name='register_user'),

    path('products/', views.getProducts, name='routes'),
    path('product/<str:pk>', views.getProduct, name='routes')
]
