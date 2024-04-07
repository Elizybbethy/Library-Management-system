# Generated by Django 4.2.6 on 2024-04-05 08:38

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("eight", "0001_initial"),
    ]

    operations = [
        migrations.CreateModel(
            name="Book",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                ("name", models.CharField(max_length=100)),
                ("genre", models.CharField(max_length=50)),
                ("availablility", models.BooleanField(default=True)),
                ("copies_number", models.IntegerField(default=1)),
            ],
        ),
    ]
