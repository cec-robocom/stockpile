from django.db import models
from accounts.models import Profile
from components.models import Component
from django.utils import timezone

# Create your models here.
class History(models.Model):
    user_id = models.ForeignKey(Profile, on_delete=models.CASCADE)
    components_taken = models.ManyToManyField(Component)
    taken_date = models.DateTimeField(default=timezone.now)
    return_date = models.DateTimeField(null=True)

    class Meta:
        verbose_name_plural = "histories"

    def __str__(self):
        return self.pk
