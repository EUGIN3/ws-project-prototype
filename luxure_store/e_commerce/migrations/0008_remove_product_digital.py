# Generated by Django 5.1.3 on 2024-11-18 15:04

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ("e_commerce", "0007_remove_order_date_remove_order_phone_and_more"),
    ]

    operations = [
        migrations.RemoveField(
            model_name="product",
            name="digital",
        ),
    ]
