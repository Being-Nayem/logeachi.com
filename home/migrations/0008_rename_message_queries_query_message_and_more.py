# Generated by Django 4.1.7 on 2023-09-18 10:54

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0007_alter_queries_query_status'),
    ]

    operations = [
        migrations.RenameField(
            model_name='queries',
            old_name='message',
            new_name='query_message',
        ),
        migrations.AddField(
            model_name='queries',
            name='query_reply',
            field=models.TextField(blank=True, default=None, max_length=1000, null=True),
        ),
        migrations.AddField(
            model_name='queries',
            name='reply_date',
            field=models.DateTimeField(auto_now=True),
        ),
    ]
