from django.urls import path
from . import views

urlpatterns = [
    path('payment/', views.initiate_payment, name='payment'),
    path('callback/',views.callback, name='callback')
]
