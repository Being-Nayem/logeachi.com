# Generated by Django 4.1.7 on 2023-09-17 12:54

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0002_subscribers_gender'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='Subscribers',
            new_name='Newsletter',
        ),
    ]