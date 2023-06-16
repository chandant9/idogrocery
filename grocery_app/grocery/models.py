from django.db import models

UNIT_CHOICES = (
    ('pcs', 'Pieces'),
    ('g', 'Grams'),
    ('kg', 'Kilograms'),
    ('L', 'Litres'),
)

# Creating models below, more models can be added to increase app features.


class GroceryItem(models.Model):
    name = models.CharField(max_length=100)
    group = models.CharField(max_length=100)
    quantity = models.PositiveIntegerField(default=0)
    unit = models.CharField(max_length=50, choices=UNIT_CHOICES, null=True)
    price = models.DecimalField(max_digits=10, decimal_places=2)
    expiration_date = models.DateField()

    def __str__(self):
        return self.name
