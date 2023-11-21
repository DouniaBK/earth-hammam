from django.shortcuts import render
from django.core.validators import validate_email
from django.core.exceptions import ValidationError
from .models import SubscribedUser


def subscribe(request):
    if request.method == 'POST':
        name = request.POST.get('name', None)
        email = request.POST.get('email', None)

        if not name or not email:
            messages.error(
                request, "You must enter a valid email to subscribe.")
            return redirect("/")

        if get_user_model().objects.filter(email=email).first():
            messages.error(
                request, f"A registered user with associated {email} found, login to proceed."
                )
            return redirect(request.META.get("HTTP_REFERER", "/"))

        subscribe_user = SubscribedUser.objects.filter(email=email).first()
        if subscribe_user:
            messages.error(
                request, f"{email} email address is already subscriber.")
            return redirect(request.META.get("HTTP_REFERER", "/"))

        try:
            validate_email(email)
        except ValidationError as e:
            messages.error(request, e.messages[0])
            return redirect("/")

        subscribe_model_instance = SubscribedUser()
        subscribe_model_instance.name = name
        subscribe_model_instance.email = email
        subscribe_model_instance.save()
        messages.success(
            request, f'{email} successfully subscribed')
        return redirect(request.META.get("HTTP_REFERER", "/"))
