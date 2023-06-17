# Generated by Django 4.2.2 on 2023-06-17 11:50

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('grocery', '0002_groceryitem_unit'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='groceryitem',
            name='group',
        ),
        migrations.AddField(
            model_name='groceryitem',
            name='category',
            field=models.CharField(choices=[('FR-VG', 'Fruits & Vegetables'), ('DAI-EG', 'Dairy & Eggs'), ('CHS', 'Cheese'), ('BAK', 'Bakery'), ('DR', 'Drinks'), ('FRZ', 'Frozen food'), ('SN-CAN', 'Snacks & Candies'), ('MT-SF', 'Meat & Seafood'), ('CLS', 'Cleaning Supplies'), ('PERS', 'Personal Care'), ('HLTH', 'Health'), ('MISC', 'Miscellaneous')], default='N/A', max_length=7),
        ),
        migrations.AlterField(
            model_name='groceryitem',
            name='unit',
            field=models.CharField(choices=[('pcs', 'Pieces'), ('g', 'Grams'), ('kg', 'Kilograms'), ('L', 'Litres'), ('packs', 'Packs')], max_length=50, null=True),
        ),
    ]