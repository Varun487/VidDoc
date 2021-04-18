from django.db import models
from Appointments.models import Appointment

# Create your models here.
class Prescription(models.Model):
    appointment = models.ForeignKey(Appointment, on_delete=models.CASCADE,  primary_key =True)
    prescription = models.CharField(max_length=500)
