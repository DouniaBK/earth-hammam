from django.shortcuts import render

# Create your views here.
def booking(request):
    """ A view to return the index page """

    return render(request, 'booking/booking.html')