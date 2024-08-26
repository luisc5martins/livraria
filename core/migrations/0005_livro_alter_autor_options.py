# Generated by Django 5.0.6 on 2024-08-26 14:14

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("core", "0004_autor"),
    ]

    operations = [
        migrations.CreateModel(
            name="Livro",
            fields=[
                ("id", models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name="ID")),
                ("titulo", models.CharField(max_length=255)),
                ("isbn", models.CharField(blank=True, max_length=32, null=True)),
                ("quantidade", models.IntegerField(blank=True, default=0, null=True)),
                ("preco", models.DecimalField(blank=True, decimal_places=2, default=0, max_digits=7, null=True)),
            ],
        ),
        migrations.AlterModelOptions(
            name="autor",
            options={"verbose_name": "Autor", "verbose_name_plural": "Autores"},
        ),
    ]
