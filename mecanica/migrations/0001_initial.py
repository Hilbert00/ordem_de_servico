# Generated by Django 4.2.7 on 2023-12-04 11:53

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = []

    operations = [
        migrations.CreateModel(
            name="Client",
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
                ("address", models.CharField(max_length=100)),
                ("phone", models.CharField(max_length=14)),
                ("code", models.CharField(max_length=5)),
                ("rg", models.CharField(max_length=7)),
            ],
        ),
        migrations.CreateModel(
            name="Part",
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
                ("name", models.CharField(max_length=45)),
                ("code", models.CharField(max_length=5)),
                ("storage", models.IntegerField()),
                ("description", models.TextField()),
                ("price", models.DecimalField(decimal_places=2, max_digits=10)),
            ],
        ),
        migrations.CreateModel(
            name="Service",
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
                ("name", models.CharField(max_length=45)),
                ("code", models.CharField(max_length=5)),
                ("description", models.TextField()),
                ("price", models.DecimalField(decimal_places=2, max_digits=10)),
            ],
        ),
        migrations.CreateModel(
            name="Team",
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
                ("name", models.CharField(max_length=45)),
            ],
        ),
        migrations.CreateModel(
            name="Worker",
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
                ("salary", models.DecimalField(decimal_places=2, max_digits=10)),
                ("name", models.CharField(max_length=45)),
                ("specialty", models.CharField(max_length=45)),
                ("address", models.CharField(max_length=100)),
                ("rg", models.CharField(max_length=7)),
                (
                    "team_id",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE, to="mecanica.team"
                    ),
                ),
            ],
        ),
        migrations.CreateModel(
            name="Vehicle",
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
                ("model", models.CharField(max_length=45)),
                ("brand", models.CharField(max_length=45)),
                ("year", models.IntegerField()),
                ("plate", models.CharField(max_length=8)),
                ("type", models.CharField(max_length=45)),
                (
                    "client_id",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        to="mecanica.client",
                    ),
                ),
            ],
        ),
        migrations.CreateModel(
            name="Order",
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
                ("price", models.DecimalField(decimal_places=2, max_digits=10)),
                ("create_date", models.DateField(auto_now_add=True)),
                ("conclusion_date", models.DateField()),
                (
                    "parts",
                    models.ManyToManyField(related_name="orders", to="mecanica.part"),
                ),
                (
                    "services",
                    models.ManyToManyField(
                        related_name="orders", to="mecanica.service"
                    ),
                ),
                (
                    "team_id",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE, to="mecanica.team"
                    ),
                ),
                (
                    "vehicle_id",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        to="mecanica.vehicle",
                    ),
                ),
            ],
        ),
    ]