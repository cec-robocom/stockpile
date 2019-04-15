from django.db import models
from jsonfield import JSONField


class Component(models.Model):
    borrower = models.CharField(max_length=100)
    components = JSONField()
    date = models.DateField(auto_now=True)

        