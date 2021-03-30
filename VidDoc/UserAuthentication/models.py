from django.db import models
from datetime import datetime


# Create your models here.
class User(models.Model):
    name = models.CharField(max_length=200)
    email = models.CharField(max_length=500)
    password = models.CharField(max_length=64)
    address = models.TextField()
    age = models.IntegerField()
    city = models.CharField(max_length=500)
    phone_number = models.CharField(max_length=500)
    created_at = models.DateTimeField(default=datetime.now, blank=True)

    def __str__(self):
        return self.name


class Doctor(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    speciality = models.CharField(max_length=500)

    def __str__(self):
        return self.user.name
