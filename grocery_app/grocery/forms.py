from django import forms
from .models import GroceryItem


class GroceryItemForm(forms.ModelForm):
    class Meta:
        model = GroceryItem
        fields = ['name', 'group', 'quantity', 'price', 'expiration_date']
