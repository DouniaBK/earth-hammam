from django.shortcuts import render, redirect
from django.core.validators import validate_email
from django.core.exceptions import ValidationError
from django.contrib import messages
from django.core.mail import EmailMessage
from .forms import NewsletterForm
from .models import SubscribedUser
from .decorators import user_is_superuser

# The subscribe function was done following lessons from Pylessons


def subscribe(request):
    if request.method == 'POST':
        name = request.POST.get('name', None)
        email = request.POST.get('email', None)

        if not name or not email:
            messages.error(
                request, "You must enter a valid email to subscribe.")
            return redirect("/")

        subscribe_user = SubscribedUser.objects.filter(email=email).first()
        if subscribe_user:
            messages.error(
                request, f"This {email} address is already subscribed.")
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


@user_is_superuser
def newsletter(request):
    if request.method == 'POST':
        form = NewsletterForm(request.POST)
        if form.is_valid():

            subject = form.cleaned_data.get('subject')
            subscribers = form.cleaned_data.get('subscribers').split(',')
            email_message = form.cleaned_data.get('message')

            num_successful = 0
            for subscriber in subscribers:
                mail = EmailMessage(
                    subject, email_message, f"Earth Hammam <{request.user.email}>",
                    bcc=[subscriber])
                mail.content_subtype = 'html'
                if mail.send():
                    num_successful = num_successful + 1
            
            if num_successful == len(subscribers):
                messages.success(request, "Newsletter succesfully sent.")
            else:
                messages.error(request, "Email sent to " + str(num_successful) + " subscribers.")

        else:
            for error in list(form.errors.values()):
                messages.error(request, error)

        return redirect('/')

    form = NewsletterForm()
    form.fields['subscribers'].initial = ','.join(
        [active.email for active in SubscribedUser.objects.all()])
    return render(
        request=request, template_name='marketing/newsletter.html',
        context={'form': form})


def unsubscribe(request):

    if request.method == 'POST':
        email = request.POST.get('email', None)
        subscribed_user = SubscribedUser.objects.filter(email=email).first()
        if subscribed_user:
            #  delete subscribed user
            subscribed_user.delete()
            #  send an email to him that he was unsubscribed
            messages.success(
                request,
                f'The following {email} address has been unsubscribed')
    return render(request, "marketing/unsubscribe.html", context={'blabla': 1})
