from django.urls import path
from . import views

urlpatterns = [
    path('', views.index_consultation, name='consult'),
    path('<int:id>', views.show_prescription,name='prescription'),
]
