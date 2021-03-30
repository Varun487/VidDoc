from django.db import models
from datetime import datetime

# Create your models here.
class User(models.Model):
    name = models.CharField(max_length=200)
    email = models.TextField()
    password = models.CharField(max_length=64)
    address = models.TextField()
    age = models.TextField()
    city = models.TextField()
    phnumber = models.TextField()
    created_at = models.DateTimeField(default=datetime.now, blank=True)

    def __str__(self):
        return self.name
