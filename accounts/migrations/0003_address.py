# Generated by Django 4.1.7 on 2023-03-08 14:19

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0002_rename_phone_user_last_name_remove_user_address_and_more'),
    ]

    operations = [
        migrations.CreateModel(
            name='Address',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('full_name', models.CharField(max_length=30)),
                ('phone', models.CharField(max_length=11)),
                ('city', models.CharField(max_length=20)),
                ('thana', models.CharField(max_length=20)),
                ('postal_code', models.CharField(max_length=10)),
                ('detail_address', models.TextField(max_length=100)),
                ('customer', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
