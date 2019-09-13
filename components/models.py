from django.db import models
from accounts.models import Profile

# Create your models here.
class Component(models.Model):
    name = models.CharField(max_length=20)
    stock = models.IntegerField(default=0)
    borrowed_by = models.ManyToManyField(Profile)

    def __str__(self):
        return self.name