# Generated by Django 2.0.3 on 2020-02-13 10:38

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('orders', '0006_auto_20200213_1036'),
    ]

    operations = [
        migrations.AlterField(
            model_name='pizza',
            name='toppings',
            field=models.IntegerField(choices=[('0', 'Cheese'), ('1', '1 Topping'), ('2', '2 Toppings'), ('3', '3 Toppings'), ('4', 'Special Toppings')], default=0),
        ),
    ]
