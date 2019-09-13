from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    ieee_id = models.CharField(max_length=12, unique=True, default=0)
    phone_number = models.CharField(max_length=14, default=0)

