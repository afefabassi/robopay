# Generated by Django 4.2 on 2023-04-11 23:33

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = []

    operations = [
        migrations.CreateModel(
            name="Form",
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
                ("montant", models.PositiveIntegerField()),
                ("image", models.ImageField(upload_to="")),
            ],
        ),
    ]
