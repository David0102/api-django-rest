from django.contrib import admin
from .models import Curso, Avaliacao

@admin.register(Curso)
class CursoAdmin(admin.ModelAdmin):
    list_display = ["titulo", "url", "criado", "modificado", "ativo"]
    search_fields = ["titulo", "descricao"]

@admin.register(Avaliacao)
class AvaliacaoAdmin(admin.ModelAdmin):
    list_display = ["curso", "nome", "email", "avaliacao", "criado", "modificado", "ativo"]
    search_fields = ["curso", "nome", "email", "avaliacao"]