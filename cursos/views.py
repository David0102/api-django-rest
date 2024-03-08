from rest_framework import generics
from django.shortcuts import get_object_or_404

from rest_framework import viewsets
from rest_framework.decorators import action
from rest_framework.response import Response
from django.contrib.auth.models import User

from cursos.permissions import IsSuperUserAuthNotPost, IsSuperUserAuthNotGet
from rest_framework.views import APIView
from rest_framework import exceptions
from rest_framework.authtoken.models import Token

from cursos.serializers import CursoSerializer, AvaliacaoSerializer, UserSerializer
from cursos.models import Curso, Avaliacao


# Extra curso
class UserViewSet(viewsets.ModelViewSet):
    permission_classes = (IsSuperUserAuthNotPost,)
    queryset = User.objects.all()
    serializer_class = UserSerializer

class TokenAuth(APIView):
    def post(self, request):
        username = request.data.get('username')
        password = request.data.get('password')

        if username is None or password is None:
            return None
        
        user = User.objects.filter(username=username).first()

        if user is None:
            raise exceptions.AuthenticationFailed('Usuário não encontrado')
        
        if not user.check_password(password):
            raise exceptions.AuthenticationFailed('Senha inválida')
        
        token = Token.objects.create(user=user)

        return Response({
            'id': user.id,
            'username': user.username,
            'token': token.key
            })

# API version 2

class CursoViewSet(viewsets.ModelViewSet):
    permission_classes = (IsSuperUserAuthNotGet,)
    queryset = Curso.objects.all()
    serializer_class = CursoSerializer

    @action(detail=True, methods=['get'])
    def avaliacoes(self, request, pk=None):
        self.pagination_class.page_size = 2
        avaliacoes = Avaliacao.objects.filter(curso_id=pk)
        page = self.paginate_queryset(avaliacoes)

        if page is not None:
            serializer = AvaliacaoSerializer(page, many=True)
            return self.get_paginated_response(serializer.data)

        serializer = AvaliacaoSerializer(avaliacoes, many=True)
        return Response(serializer.data)


class AvaliacaoViewSet(viewsets.ModelViewSet):
    queryset = Avaliacao.objects.all()
    serializer_class = AvaliacaoSerializer



# API version 1
"""
class CursosAPIView(generics.ListCreateAPIView):
    queryset = Curso.objects.all()
    serializer_class = CursoSerializer


class CursoAPIView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Curso.objects.all()
    serializer_class = CursoSerializer


class AvaliacoesAPIView(generics.ListCreateAPIView):
    queryset = Avaliacao.objects.all()
    serializer_class = AvaliacaoSerializer

    def get_queryset(self):
        if self.kwargs.get('curso_pk'):
            return self.queryset.filter(curso_id=self.kwargs.get('curso_pk'))
        return self.queryset.all()


class AvaliacaoAPIView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Avaliacao.objects.all()
    serializer_class = AvaliacaoSerializer

    def get_object(self):
        if self.kwargs.get('curso_pk'):
            return get_object_or_404(self.get_queryset(), curso_id=self.kwargs.get('curso_pk'), 
                                     pk=self.kwargs.get('avaliacao_pk'))
        return get_object_or_404(self.get_queryset(), pk=self.kwargs.get('avaliacao_pk'))
"""