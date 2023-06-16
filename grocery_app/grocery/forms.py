from django import forms
from .models import GroceryItem
# from tempus_dominus.widgets import DateTimePicker
# from bootstrap_datepicker_plus import DateTimePickerInput


class GroceryItemForm(forms.ModelForm):
    class Meta:
        model = GroceryItem
        fields = ['name', 'group', 'quantity', 'price', 'expiration_date']
        expiration_date = forms.DateField(widget=forms.DateInput(attrs={'type': 'date'}))
