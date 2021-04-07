from django.contrib import admin
from .models import Appointment, Prescription, Medicines

# Register your models here.
admin.site.register(Appointment)
admin.site.register(Prescription)
admin.site.register(Medicines)
