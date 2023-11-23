from django import forms
from tinymce.widgets import TinyMCE


class NewsletterForm(forms.Form):
    subject = forms.CharField()
    subscribers = forms.CharField()
    message = forms.CharField(widget=TinyMCE(), label="Email content")
