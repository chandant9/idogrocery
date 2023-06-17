from django.shortcuts import render, redirect, get_object_or_404
from .models import GroceryItem
from django.http import JsonResponse
from .forms import GroceryItemForm

# Creating views below as required


def grocery_list(request):
    form = GroceryItemForm(request.POST or None)
    if request.method == 'POST' and form.is_valid():
        form.save()
        return redirect('grocery_list')
    groceries = GroceryItem.objects.all()

    # To calculate total quantity and prices on both total and category level
    category_totals = dict()
    total_quantity = 0
    total_price = 0

    # Iterating through each item.
    for grocery in groceries:
        category = grocery.category
        quantity = grocery.quantity
        price = grocery.price

        # Assigning values for each category for quantity and price and summing it up
        if category in category_totals:
            category_totals[category]['quantity'] += quantity
            category_totals[category]['price'] += price
        else:
            category_totals[category] = {'quantity': quantity, 'price': price}

        # calculating overall totals here
        total_quantity += quantity
        total_price += price

    context = {
        'form': form,
        'groceries': groceries,
        'category_totals': category_totals,
        'total_quantity': total_quantity,
        'total_price': total_price,
    }
    return render(request, 'grocery/list.html', context)


def grocery_detail(request, item_id):
    grocery = GroceryItem.objects.get(pk=item_id)
    context = {
        'grocery': grocery,
    }
    return render(request, 'grocery/detail.html', context)


def grocery_edit(request, item_id):
    grocery = get_object_or_404(GroceryItem, pk=item_id)
    if request.method == 'POST':
        form = GroceryItemForm(request.POST, instance=grocery)
        if form.is_valid():
            form.save()
            return redirect('grocery_list')
    else:
        form = GroceryItemForm(instance=grocery)

    return render(request, 'grocery/edit.html', {'form': form})


def grocery_delete(request, item_id):
    grocery = get_object_or_404(GroceryItem, pk=item_id)
    if request.method == 'POST':
        grocery.delete()
        return redirect('grocery_list')

    return render(request, 'grocery/list.html', {'grocery': grocery})


def cart_json(request):
    cart_data = {
        'cart_id': '123',  # Replace with cart id or data
        'total_items': 5,  # Replace with qty
    }

    return JsonResponse(cart_data)
