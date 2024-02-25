from django.db import models
from datetime import datetime
from django.utils import timezone
from products.models import Item
from checkout.models import Order
from django.contrib.auth.models import User
from profiles.models import UserProfile

from datetime import timedelta, date, time


class Appointment(models.Model):
    user = models.ForeignKey(
        UserProfile, on_delete=models.CASCADE, null=True, blank=True
    )
    item = models.ForeignKey(
        Item,
        on_delete=models.CASCADE,
        null=True,
        blank=True,
        limit_choices_to={"category": 1},
    )
    order = models.ForeignKey(Order, on_delete=models.CASCADE, null=True, blank=True)
    time = models.DateTimeField(default=datetime.now, blank=True)
    duration = models.DurationField(default=timedelta(minutes=60))

    def __str__(self):
        return f"time: {self.time}"
