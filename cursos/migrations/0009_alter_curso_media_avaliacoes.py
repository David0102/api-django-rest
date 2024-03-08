# Generated by Django 4.2.11 on 2024-03-08 19:02

from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("cursos", "0008_curso_media_avaliacoes"),
    ]

    operations = [
        migrations.AlterField(
            model_name="curso",
            name="media_avaliacoes",
            field=models.DecimalField(
                blank=True, decimal_places=2, default=0.0, max_digits=5, null=True
            ),
        ),
    ]