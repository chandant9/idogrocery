from django.db import models

UNIT_CHOICES = (
    ('pcs', 'Pieces'),
    ('g', 'Grams'),
    ('kg', 'Kilograms'),
    ('L', 'Litres'),
    ('packs', 'Packs'),
)

CAT_CHOICES = (
    ('', 'Select Category'),
    ('FR-VG', 'Fruits & Vegetables'),
    ('DAI-EG', 'Dairy & Eggs'),
    ('CHS', 'Cheese'),
    ('BAK', 'Bakery'),
    ('DR', 'Drinks'),
    ('FRZ', 'Frozen food'),
    ('SN-CAN', 'Snacks & Candies'),
    ('MT-SF', 'Meat & Seafood'),
    ('CLS', 'Cleaning Supplies'),
    ('PERS', 'Personal Care'),
    ('HLTH', 'Health'),
    ('MISC', 'Miscellaneous'),
)


# Creating models below, more models can be added to increase app features.


class GroceryItem(models.Model):
    name = models.CharField(max_length=100, null=True)
    category = models.CharField(max_length=7, choices=CAT_CHOICES, null=True)
    quantity = models.PositiveIntegerField(default=0)
    unit = models.CharField(max_length=50, choices=UNIT_CHOICES, null=True)
    price = models.DecimalField(max_digits=10, decimal_places=2, null=True)
    expiration_date = models.DateField()

    def __str__(self):
        return self.name
