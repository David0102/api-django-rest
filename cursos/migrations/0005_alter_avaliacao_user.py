# Generated by Django 4.2.11 on 2024-03-08 15:46

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):
    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ("cursos", "0004_alter_avaliacao_user"),
    ]

    operations = [
        migrations.AlterField(
            model_name="avaliacao",
            name="user",
            field=models.ForeignKey(
                blank=True,
                null=True,
                on_delete=django.db.models.deletion.CASCADE,
                related_name="avaliacoes",
                to=settings.AUTH_USER_MODEL,
            ),
        ),
    ]
