# Generated by Django 4.2 on 2023-04-12 12:17

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ("pages", "0006_delete_forms"),
    ]

    operations = [
        migrations.CreateModel(
            name="Formulaire",
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
                ("prenom", models.CharField(max_length=20)),
                ("nom", models.CharField(max_length=20)),
            ],
        ),
    ]
