# Generated by Django 4.1.7 on 2023-09-26 09:14

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('order', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='order',
            name='order_id',
            field=models.CharField(default='lNGLdGIus2', editable=False, max_length=10, unique=True),
        ),
    ]
