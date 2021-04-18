from django.db import models
from django.utils import timezone
from datetime import datetime
from UserAuthentication.models import User, Doctor


class Appointment(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    doctor = models.ForeignKey(Doctor, on_delete=models.CASCADE)
    link = models.CharField(max_length=100)
    title = models.CharField(max_length=100)
    description = models.TextField()
    from_date_time = models.DateTimeField(default=timezone.now())
    to_date_time = models.DateTimeField(default=timezone.now())

    def __str__(self):
        return self.title
