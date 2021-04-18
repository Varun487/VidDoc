from django.urls import path
from . import views

urlpatterns = [
    path('', views.index_recommendations, name='recommendations'),
    path('selectdoctor', views.index_select_doctor, name='selectdoctor'),
    path('filterdoctors', views.index_filter_doctor, name='filterdoctor'),
]
