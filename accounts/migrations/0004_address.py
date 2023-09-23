# Generated by Django 4.1.7 on 2023-09-23 08:59

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0003_alter_user_user_image'),
    ]

    operations = [
        migrations.CreateModel(
            name='Address',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('country', models.CharField(choices=[('Bangladesh', 'Bangladesh')], default='Bangladesh', max_length=50)),
                ('zila', models.CharField(max_length=100)),
                ('thana', models.CharField(max_length=100)),
                ('postal_code', models.CharField(max_length=20)),
                ('details_address', models.CharField(max_length=255)),
                ('is_default_shipping', models.BooleanField(default=False)),
                ('is_default_billing', models.BooleanField(default=False)),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='user_address', to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
