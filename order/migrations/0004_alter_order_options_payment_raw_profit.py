# Generated by Django 4.2.5 on 2023-10-09 22:18

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('order', '0003_alter_payment_order'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='order',
            options={'ordering': ['-created_at']},
        ),
        migrations.AddField(
            model_name='payment',
            name='raw_profit',
            field=models.DecimalField(blank=True, decimal_places=2, default=0.0, max_digits=15, null=True),
        ),
    ]
