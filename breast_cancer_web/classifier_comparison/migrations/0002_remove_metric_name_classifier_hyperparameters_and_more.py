# Generated by Django 4.2.6 on 2024-02-15 14:20

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):
    dependencies = [
        ("classifier_comparison", "0001_initial"),
    ]

    operations = [
        migrations.RemoveField(
            model_name="metric",
            name="name",
        ),
        migrations.AddField(
            model_name="classifier",
            name="hyperparameters",
            field=models.TextField(default="hoal"),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name="classifier",
            name="short_description",
            field=models.TextField(default="hola"),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name="metric",
            name="confusion_matrix",
            field=models.ImageField(default=1, upload_to="confusion_matrices/"),
            preserve_default=False,
        ),
        migrations.CreateModel(
            name="GlobalShap",
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
                (
                    "classifier",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        to="classifier_comparison.classifier",
                    ),
                ),
            ],
        ),
    ]
