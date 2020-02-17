# Generated by Django 2.0.3 on 2020-02-13 15:16

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('orders', '0011_auto_20200213_1503'),
    ]

    operations = [
        migrations.CreateModel(
            name='Primo',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=64)),
                ('price', models.DecimalField(decimal_places=2, default=0, max_digits=8)),
            ],
        ),
    ]
