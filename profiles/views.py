from django.shortcuts import render, get_object_or_404
from django.contrib import messages
from django.contrib.auth.decorators import login_required

from .models import UserProfile
from .forms import UserProfileForm

from checkout.models import Order


@login_required
def profile(request):
    """ Display the user's profile. """
    profile = get_object_or_404(UserProfile, user=request.user)

    if request.method == 'POST':
        form = UserProfileForm(request.POST, instance=profile)
        if form.is_valid():
            form.save()
            messages.success(request, 'Profile updated successfully')
        else:
            messages.error(
                request, 'Update failed. Check if the form is valid.')
    else:
        form = UserProfileForm(instance=profile)
    orders = profile.orders.all()

    template = 'profiles/profile.html'
    context = {
        'form': form,
        'orders': orders,
        'on_profile_page': True
    }

    return render(request, template, context)

@login_required
def delete(request):

    try:
        user = request.user
        if not user.is_superuser:
            user.delete()
            messages.success(request, 'Your account was successfully deleted.')
        else:
            messages.success(request, 'Superuser account cannot be deleted')

    except Exception as e:
        return render(request, 'home/index.html')

    return render(request, 'home/index.html')


def order_history(request, order_number):
    order = get_object_or_404(Order, order_number=order_number)

    messages.info(request, (
        f'This is a past confirmation for order number {order_number}. '
        'A confirmation email was sent on the order date.'
    ))

    total = float(order.order_total)
    grand_total = float(order.grand_total)
    delivery = float(order.delivery_cost)

    template = 'checkout/checkout_success.html'
    context = {
        'order': order,
        'total_main': total,
        'grand_total_main': grand_total,
        'delivery_main': delivery,
        'from_profile': True,
    }

    return render(request, template, context)
