# Generated by Django 5.1.3 on 2024-11-19 01:13

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ("e_commerce", "0009_product_digital"),
    ]

    operations = [
        migrations.RemoveField(
            model_name="product",
            name="digital",
        ),
    ]
