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
    return render(request, 'grocery/list.html', {'groceries': groceries, 'form': form})


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


def cart_json(request):
    cart_data = {
        'cart_id': '123',  # Replace with cart id or data
        'total_items': 5,  # Replace with qty
    }

    return JsonResponse(cart_data)
