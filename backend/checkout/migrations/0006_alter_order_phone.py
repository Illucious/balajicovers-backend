# Generated by Django 4.2.5 on 2023-10-31 17:35

from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("checkout", "0005_order_order_id"),
    ]

    operations = [
        migrations.AlterField(
            model_name="order",
            name="phone",
            field=models.BigIntegerField(),
        ),
    ]
