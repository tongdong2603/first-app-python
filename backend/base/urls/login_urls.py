from django.urls import path
from ..views import login_views as views
from django.contrib.auth import views as auth_views

urlpatterns = [

    path('login/', views.login, name='routes'),
    path("logout/", auth_views.LogoutView.as_view(), name="logout"),
    path("", views.home, name="home"),
]
