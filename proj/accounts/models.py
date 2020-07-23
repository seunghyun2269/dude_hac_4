from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class Signup(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    address = models.CharField(max_length=30)
    college =  models.CharField(max_length=20)
    email = models.CharField(max_length=100)
    grade = models.FloatField(null=True, blank=True, default=None)
    comment = models.CharField(max_length=100)

    def __str__(self):
        return self.user