from rest_framework import serializers
from .models import Curso, Avaliacao

class AvaliacaoSerializer(serializers.ModelSerializer):
    class Meta:
        extra_kwargs = {
            'email': {'write_only': True}
        }
        model = Avaliacao
        fields = (
            'id',
            'curso',
            'nome',
            'email',
            'comentario',
            'avaliacao',
            'criado',
            'ativo'
        )

class CursoSerializer(serializers.ModelSerializer):
    #avaliacoes = AvaliacaoSerializer(many=True, read_only=True)

    #avaliacoes = serializers.HyperlinkedRelatedField(many=True, read_only=True, view_name='avaliacao-detail')

    #avaliacoes = serializers.PrimaryKeyRelatedField(many=True, read_only=True)

    class Meta:
        model = Curso
        fields = (
            'id',
            'titulo',
            'url',
            'criado',
            'ativo',
            #'avaliacoes'
        )