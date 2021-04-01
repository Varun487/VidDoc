from django.urls import path
from . import views

urlpatterns = [
    path('/consult', views.consult, name='consult'),
]
