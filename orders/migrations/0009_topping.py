# Generated by Django 2.0.3 on 2020-02-13 13:58

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('orders', '0008_auto_20200213_1309'),
    ]

    operations = [
        migrations.CreateModel(
            name='Topping',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('topping', models.CharField(choices=[('PEPPERONI', 'Pepperoni'), ('SAUSAGE', 'Sausage'), ('MUSHROOMS', 'Mushrooms'), ('ONIONS', 'Onions'), ('HAM', 'Ham'), ('CANADIAN HAM', 'Canadian Ham'), ('PINEAPPLE', 'Pineapple'), ('EGGPLANT', 'Eggplant'), ('TOMATO AND BASIL', 'Tomato & Basil'), ('GREEN PEPPERS', 'Green Peppers'), ('HAMBURGER', 'Hamburger'), ('SPINACH', 'Spinach'), ('ARTICHOKE', 'Artichoke'), ('BUFFALO CHICKEN', 'Buffalo Chicken'), ('BARBECUE CHICKEN', 'Barbecue Chicken'), ('ANCHOVIES', 'Anchovies'), ('BLACK OLIVES', 'Black Olives'), ('FRESH GARLIC', 'Fresh Garlic'), ('ZUCCHINI', 'Zucchini')], max_length=64)),
            ],
        ),
    ]
