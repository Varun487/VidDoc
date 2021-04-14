from django.urls import path
from . import views

urlpatterns = [
    path('', views.index_login, name='index'),
    path('login/', views.index_login, name='login'),
    path('register/', views.index_register, name='register'),
    path('login/userauth/', views.auth_login, name='login auth function'),
    path('register/userauth/', views.auth_register, name='register auth function'),
    path('logout/', views.index_logout, name='logout'),
]
