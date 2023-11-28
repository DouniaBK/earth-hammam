from django.shortcuts import render
from .models import Testimonial

# Create your views here.


def index(request):
    """ A view to return the index page """

    return render(request, 'home/index.html')


def hammam(request):
    all_testimonials = Testimonial.objects.filter(status='1')
    return render(request, 'home/hammam.html', {'all_testimonials': all_testimonials})  # noqa


def privacypolicy(request):
    return render(request, 'home/privacy_policy.html')


def certification(request):
    return render(request, 'home/certification.html')
