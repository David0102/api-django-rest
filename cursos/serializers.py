from rest_framework import serializers
from .models import Curso, Avaliacao
from django.contrib.auth.models import User
from django.db import IntegrityError
from django.db import models

class AvaliacaoSerializer(serializers.ModelSerializer):
    user = serializers.ReadOnlyField(source='user.username', required=False)

    class Meta:
        model = Avaliacao
        fields = (
            'id',
            'curso',
            'user',
            'comentario',
            'avaliacao',
            'criado',
            'ativo'
        )
    
    def validate_avaliacao(self, valor):
        if 1<= valor <= 5:
            return valor
        raise serializers.ValidationError('A avaliação precisa ser entre 1 e 5')

    def create(self, validated_data):
        try:
            return super().create(validated_data)
        except IntegrityError:
            raise serializers.ValidationError('Você já avaliou este curso')

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
            'media_avaliacoes'
            #'avaliacoes'
        )
    

# extra curso
class UserSerializer(serializers.ModelSerializer):
    class Meta:
        extra_kwargs = {
            'password': {'write_only': True}
        }
        model = User
        fields = (
            'id',
            'username',
            'email',
            'password'
        )

    def create(self, validated_data):
        email = validated_data['email']
        if User.objects.filter(email=email).exists():
            raise serializers.ValidationError({"email": "Email já existe"})
        user = User(
            username=validated_data['username'],
            email=validated_data['email']
        )
        user.set_password(validated_data['password'])
        user.save()
        return user