# Generated by Django 4.2.11 on 2024-03-08 16:04

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):
    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ("cursos", "0005_alter_avaliacao_user"),
    ]

    operations = [
        migrations.AlterField(
            model_name="avaliacao",
            name="user",
            field=models.ForeignKey(
                default=1,
                on_delete=django.db.models.deletion.CASCADE,
                related_name="avaliacoes",
                to=settings.AUTH_USER_MODEL,
            ),
        ),
    ]
