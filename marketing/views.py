from django.shortcuts import render, redirect
from django.core.validators import validate_email
from django.core.exceptions import ValidationError
from django.contrib import messages
from django.core.mail import EmailMessage
from .forms import NewsletterForm
from .models import SubscribedUser
from .decorators import user_is_superuser


def subscribe(request):
    if request.method == 'POST':
        name = request.POST.get('name', None)
        email = request.POST.get('email', None)

        if not name or not email:
            messages.error(
                request, "You must enter a valid email to subscribe.")
            return redirect("/")
        '''
        if django.contrib.auth.get_user_model().objects.filter(email=email).first():
            messages.error(
                request, f"A registered user with associated {email} found, login to proceed."
            )
            return redirect(request.META.get("HTTP_REFERER", "/"))
        '''
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
            receivers = form.cleaned_data.get('receivers').split(',')
            email_message = form.cleaned_data.get('message')

            mail = EmailMessage(
                subject, email_message, f"Earth Hammam <{request.user.email}>", bcc=receivers)
            mail.content_subtype = 'html'

            if mail.send():
                messages.success(request, "Newsletter succesfully sent.")
            else:
                messages.error(request, "There was an error sending email")

        else:
            for error in list(form.errors.values()):
                messages.error(request, error)

        return redirect('home')

    form = NewsletterForm()
    form.fields['receivers'].initial = ','.join(
        [active.email for active in SubscribedUser.objects.all()])
    return render(
        request=request, template_name='marketing/newsletter.html', context={'form': form})


def unsubscribe(request):
    return render(request, "marketing/unsubscribe.html")

def unsubscribed(request):
    
    try:
        if request.method == 'POST':
            email = request.POST.get('email', None)
            subscribed_user = SubscribedUser.objects.filter(email=email).first()
            #  delete subscribed user
            subscribed_user.delete()
            #  send an email to him that he was unsubscribed
            messages.success(
                request, f'The following {email} addess has successfully been unsubscribed')
        return render(request, "marketing/unsubscribe.html", context={'blabla': 1})
    except ImportError as exc:
        print(exc)

