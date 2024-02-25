from django import forms
from .models import Appointment
from products.models import Item
from django.contrib.auth.models import User
from django.forms import ModelForm
from django.contrib.admin.widgets import (
    AdminDateWidget,
    AdminTimeWidget,
    AdminSplitDateTime,
)


class AppointmentInputForm(forms.ModelForm):
    service = forms.ModelChoiceField(queryset=Item.objects.filter(category=1))
    time = forms.SplitDateTimeField(widget=AdminSplitDateTime())

    class Meta:
        model = Appointment
        fields = ("user", "item", "time")
        labels = {
            "user": "Email",
            "item": "Item",
            "time": "Appointment",
        }
        widgets = {
            "time": AdminSplitDateTime(),
        }


class AppointmentInputFormFrontEnd(forms.ModelForm):
    service = forms.ModelChoiceField(queryset=Item.objects.filter(category=1))
    time = forms.SplitDateTimeField(label="", widget=AdminSplitDateTime())

    class Meta:
        model = Appointment
        fields = ("service", "time")
        labels = {
            "service": "Treatment",
            "time": "Appointment",
        }
        widgets = {}
