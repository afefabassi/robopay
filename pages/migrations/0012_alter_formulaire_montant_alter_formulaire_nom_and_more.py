# Generated by Django 4.2 on 2023-04-12 13:24

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("pages", "0011_alter_formulaire_montant"),
    ]

    operations = [
        migrations.AlterField(
            model_name="formulaire",
            name="montant",
            field=models.IntegerField(default=None),
        ),
        migrations.AlterField(
            model_name="formulaire",
            name="nom",
            field=models.CharField(default=None, max_length=20),
        ),
        migrations.AlterField(
            model_name="formulaire",
            name="prenom",
            field=models.CharField(default=None, max_length=20),
        ),
    ]
