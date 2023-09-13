# Generated by Django 4.1.7 on 2023-09-13 00:26

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Category',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=255)),
            ],
            options={
                'verbose_name_plural': '1. Categories',
            },
        ),
        migrations.CreateModel(
            name='Subcategory',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=255)),
                ('category', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='category', to='products.category')),
            ],
            options={
                'verbose_name_plural': '2. Sub Categories',
            },
        ),
        migrations.CreateModel(
            name='Product',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('product_name', models.CharField(max_length=100)),
                ('product_image', models.ImageField(upload_to='product')),
                ('product_brand', models.CharField(default='No Brand', max_length=100)),
                ('product_slug', models.SlugField(blank=True, null=True, unique=True)),
                ('product_price', models.IntegerField()),
                ('product_description', models.TextField()),
                ('product_quantity', models.IntegerField(null=True)),
                ('product_sold_quantity', models.IntegerField(default=0)),
                ('product_location', models.CharField(max_length=100)),
                ('product_warrenty', models.BooleanField()),
                ('product_cash_payment', models.BooleanField()),
                ('product_online_payment', models.BooleanField()),
                ('product_return', models.BooleanField()),
                ('product_added_date', models.DateTimeField(auto_now_add=True, null=True)),
                ('product_stock_date', models.DateTimeField(auto_now=True, null=True)),
                ('product_category', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='products', to='products.subcategory')),
            ],
            options={
                'verbose_name_plural': '3. Products',
                'ordering': ['-product_added_date'],
            },
        ),
    ]
