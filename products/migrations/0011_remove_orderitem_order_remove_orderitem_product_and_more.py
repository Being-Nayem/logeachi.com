# Generated by Django 4.1.7 on 2023-03-10 09:13

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('products', '0010_order_orderitem'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='orderitem',
            name='order',
        ),
        migrations.RemoveField(
            model_name='orderitem',
            name='product',
        ),
        migrations.DeleteModel(
            name='Order',
        ),
        migrations.DeleteModel(
            name='OrderItem',
        ),
    ]
