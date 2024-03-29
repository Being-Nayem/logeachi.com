# Generated by Django 4.1.7 on 2023-10-06 21:36

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('products', '0003_rename_roduct_flash_expiry_product_product_flash_expiry'),
        ('home', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='shop_by_deals',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('deals_name', models.CharField(blank=True, max_length=155, null=True)),
                ('delas_image', models.ImageField(upload_to='delas')),
                ('category', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='products.category')),
            ],
        ),
    ]
