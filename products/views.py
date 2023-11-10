from django.shortcuts import render, redirect, reverse, get_object_or_404
from django.contrib import messages
from .models import Item, Category
from .forms import ItemForm

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


def add_item(request):
    """ Add a product to the store """
    if request.method == 'POST':
        form = ItemForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            messages.success(request, 'Successfully added product!')
            return redirect(reverse('add_item'))
        else:
            messages.error(
                request, 'Failed to add product. Please ensure the form is valid.')
    else:
        form = ItemForm()

    template = 'products/add_item.html'
    context = {
        'form': form,
    }

    return render(request, template, context)


def edit_item(request, item_id):
    """ Edit a product in the store """
    item = get_object_or_404(Item, pk=item_id)
    if request.method == 'POST':
        form = ItemForm(request.POST, request.FILES, instance=item)
        if form.is_valid():
            form.save()
            messages.success(
                request, f'You have successfully updated {item.name}.')
            return redirect(reverse('edit_item', args=[item.id]))
        else:
            messages.error(
                request, 'Failed to update this Item. Please, ensure the form is valid.')
    else:
        form = ItemForm(instance=item)
        messages.info(request, f'You are editing {item.name}')

    template = 'products/edit_item.html'
    context = {
        'form': form,
        'item': item,
    }

    return render(request, template, context)


def delete_item(request, item_id):
    """ Delete a product from the store """
    item = get_object_or_404(Item, pk=item_id)
    item.delete()
    messages.success(request, 'Item deleted from the Online Store!')
    return redirect(reverse('add_item'))
