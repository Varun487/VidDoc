from django.urls import path
from . import views

urlpatterns = [
    path('', views.index_appointments, name='appointments'),
    path('bookappointment', views.index_book_appointment, name='book_appointment'),
    path('appointment_info', views.index_appointment_info, name='appointment_info'),
    path('cancelappointment/<int:id>', views.index_cancel_appointment, name='cancel_appointment'),
]
