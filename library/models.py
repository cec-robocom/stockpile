from django.db import models
from django.contrib.auth.models import User
from django.utils import timezone


class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    ieee_id = models.CharField(max_length=12, unique=True, default=0)
    phone_number = models.CharField(max_length=14, default=0)


class Components(models.Model):
    name = models.CharField(max_length=20)
    stock = models.IntegerField(default=0)
    borrowed_by = models.ManyToManyField(Profile)

    def __str__(self):
        return self.name


class History(models.Model):
    user_id = models.ForeignKey(Profile, on_delete=models.CASCADE)
    components_taken = models.ManyToManyField(Components)
    taken_date = models.DateTimeField(default=timezone.now)
    return_date = models.DateTimeField(null=True)

    def __str__(self):
        return self.pk
