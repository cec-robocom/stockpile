from django.db import models
from django.utils import timezone


class user(models.Model):
    name = models.CharField(max_length=30)
    email = models.EmailField()
    phone_number = models.CharField(max_length=12)
    ieee_id = models.CharField(max_length=10)

    def __str__(self):
        return self.pk


class component(models.Model):
    name = models.CharField(max_length=30)
    stock = models.IntegerField()
    borrowed_by = models.ManyToManyField(user)

    def __str__(self):
        return self.pk


class history(models.Model):
    user_id = models.ForeignKey(user, on_delete=models.CASCADE)
    component_taken = models.ForeignKey(component, on_delete=models.CASCADE)
    taken_date = models.DateTimeField(default=timezone.now)
    return_date = models.DateTimeField(null=True)

    def __str__(self):
        return self.pk
