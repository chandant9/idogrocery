from django.shortcuts import render
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
    return render(request, 'grocery/detail.html', {'grocery': grocery})


def cart_json(request):
    cart_data = {
        'cart_id': '123',  # Replace with cart id or data
        'total_items': 5,  # Replace with qty
    }

    return JsonResponse(cart_data)
