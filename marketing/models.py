from django.db import models
from django.utils import timezone
# Create your models here.


class SubscribedUser(models.Model):
    name = models.CharField(max_length=100)
    email = models.EmailField(unique=True, max_length=100)
    subscription_date = models.DateTimeField(
        'Subscription Date', default=timezone.now)

    def __str__(self):
        return self.email
