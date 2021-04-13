from django.db import models
from datetime import datetime
from UserAuthentication.models import User, Doctor

FOOD_CHOICES = (
    ("1", "Before food"),
    ("2", "After food"),
)


# Create your models here.
class Appointment(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    doctor = models.ForeignKey(Doctor, on_delete=models.CASCADE)
    link = models.CharField(max_length=100)
    title = models.CharField(max_length=100)
    description = models.TextField()
    date = models.DateTimeField()

    def __str__(self):
        return self.title
