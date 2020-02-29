# Generated by Django 2.0.3 on 2020-02-29 05:37

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('orders', '0007_auto_20200229_0032'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='addeditem',
            name='extras',
        ),
        migrations.AddField(
            model_name='addeditem',
            name='extras',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='orders.ExtraSelection'),
        ),
        migrations.RemoveField(
            model_name='extraselection',
            name='item',
        ),
        migrations.AddField(
            model_name='extraselection',
            name='item',
            field=models.ManyToManyField(to='orders.MenuItem'),
        ),
    ]
