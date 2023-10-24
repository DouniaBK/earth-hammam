from django.shortcuts import render, get_object_or_404
from .models import Item, Category

# Create your views here.


def all_items(request):
    """ A view to show all items in category products """

    items = Item.objects.filter(category_id='3')
    return render(request, 'products/products.html', {'items': items})


def all_treatments(request):
    """ A view to show all items in category treatments """

    treatments = Item.objects.filter(category_id='1')
    return render(request, 'products/treatments.html', {'treatments': treatments})


def all_tickets(request):
    """ A view to show all items in category tickets """

    tickets = Item.objects.filter(category_id='2')
    return render(request, 'products/tickets.html', {'tickets': tickets})

def tickets(request):
    return render(request, 'tickets.html', {})


def item_detail(request, product_id):
    """ A view to show individual product details """

    item = get_object_or_404(Item, pk=product_id)

    context = {
        'item': item,
    }

    return render(request, 'products/item_detail.html', context)