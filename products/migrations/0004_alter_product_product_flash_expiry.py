# Generated by Django 4.2.5 on 2023-10-08 13:45

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('products', '0003_rename_roduct_flash_expiry_product_product_flash_expiry'),
    ]

    operations = [
        migrations.AlterField(
            model_name='product',
            name='product_flash_expiry',
            field=models.DateField(blank=True, null=True),
        ),
    ]