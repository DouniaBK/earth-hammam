
from django.contrib import admin
from .models import Appointment
from .forms import AppointmentInputForm


# Appointment model is in the booking app

@admin.register(Appointment)
class AppointmentAdmin(admin.ModelAdmin):
    model = Appointment
    list_display = ("user", "item", "time", "duration")
    list_filter = ("user", "item", "time", "duration")
    search_fields = ("user", "item", "time", "duration")
    ordering = ('time',)

    form = AppointmentInputForm
