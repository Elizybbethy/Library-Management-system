# Generated by Django 4.2.6 on 2024-04-05 11:54

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("eight", "0004_remove_borrowedbook_user_borrowedbook_client_name"),
    ]

    operations = [
        migrations.AddField(
            model_name="borrowedbook",
            name="book_copies",
            field=models.IntegerField(default=1),
        ),
    ]
