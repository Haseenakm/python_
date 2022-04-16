from django.contrib.auth.models import AbstractUser
from django.db import models

# Create your models here.
class Login(AbstractUser):
    is_user = models.BooleanField(default=False)
class Email(models.Model):
    Email = models.EmailField(max_length=75)
    Phone = models.IntegerField(max_length=10)
