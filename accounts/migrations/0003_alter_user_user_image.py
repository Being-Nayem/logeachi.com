# Generated by Django 4.1.7 on 2023-09-22 20:10

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0002_user_user_image'),
    ]

    operations = [
        migrations.AlterField(
            model_name='user',
            name='user_image',
            field=models.ImageField(blank=True, default=None, null=True, upload_to=''),
        ),
    ]
