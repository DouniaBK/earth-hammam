from django.shortcuts import (
    render, redirect, reverse, HttpResponse, get_object_or_404
)
from django.contrib import messages

from products.models import Item

# Create your views here.


def view_bag(request):
    """ A view that renders the bag contents page """

    user_is_logged_in = request.user.is_authenticated

    return render(request, 'bag/bag.html', {'user_is_logged_in': user_is_logged_in})


def add_to_bag(request, item_id):
    """ Add a quantity of the specified product to the shopping bag """

    # Get items and bag
    item = get_object_or_404(Item, pk=item_id)
    # Add default quantity 1
    quantity = 1
    redirect_url = request.POST.get('redirect_url')
    bag = request.session.get('bag', {})

    # Update quantity or add item
    if item_id in list(bag.keys()):
        bag[item_id] += quantity
        messages.success(
            request,
            f'You have updated {item.name} quantity to {bag[item_id]}')
    else:
        bag[item_id] = quantity
        messages.success(request, f'You have added {item.name} to your bag')

    request.session['bag'] = bag
    print(request.session['bag'])
    return redirect(redirect_url)


def adjust_bag(request, item_id):
    """Adjust the quantity of the specified product to the specified amount"""

    # Get items and bag, then update the bag
    item = get_object_or_404(Item, pk=item_id)
    quantity = int(request.POST.get('quantity'))
    bag = request.session.get('bag', {})
    if quantity > 0:
        bag[item_id] = quantity
        messages.success(
            request,
            f'You have updated {item.name} quantity to {bag[item_id]}')
    else:
        bag.pop(item_id)

    request.session['bag'] = bag
    return redirect(reverse('view_bag'))


def remove_from_bag(request, item_id):
    """Remove the item from the shopping bag"""

    try:
        item = get_object_or_404(Item, pk=item_id)
        size = None
        if 'product_size' in request.POST:
            size = request.POST['product_size']
        bag = request.session.get('bag', {})

        if size:
            del bag[item_id]['items_by_size'][size]
            if not bag[item_id]['items_by_size']:
                bag.pop(item_id)
        else:
            bag.pop(item_id)

        request.session['bag'] = bag
        return HttpResponse(status=200)

    except Exception as e:
        messages.error(request, f'Error removing item: {e}')
        return HttpResponse(status=500)
