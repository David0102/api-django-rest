# Generated by Django 4.2.11 on 2024-03-08 19:04

from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("cursos", "0009_alter_curso_media_avaliacoes"),
    ]

    operations = [
        migrations.AlterField(
            model_name="curso",
            name="media_avaliacoes",
            field=models.DecimalField(decimal_places=2, default=0.0, max_digits=5),
        ),
    ]
