from django.urls import path, include

from rest_framework.routers import SimpleRouter

from .views import (
    #CursosAPIView, 
    #AvaliacoesAPIView, 
    #ursoAPIView, 
    #AvaliacaoAPIView,
    CursoViewSet,
    AvaliacaoViewSet,
    UserViewSet,
    TokenAuth
)


# API version 2
router = SimpleRouter()
router.register('cursos', CursoViewSet)
router.register('avaliacoes', AvaliacaoViewSet)
router.register('usuarios', UserViewSet)

urlpatterns = [
    path('', include(router.urls)),
    path('login', TokenAuth.as_view(), name='login'),
]


# API version 1

"""
urlpatterns = [
    path('cursos/', CursosAPIView.as_view(), name='cursos'),
    path('cursos/<int:pk>/', CursoAPIView.as_view(), name='curso'),
    path('cursos/<int:curso_pk>/avaliacoes/', AvaliacoesAPIView.as_view(), name='curso_avaliacoes'),
    path('cursos/<int:curso_pk>/avaliacoes/<int:avaliacao_pk>/', AvaliacaoAPIView.as_view(), name='curso_avaliacao'),
    path('avaliacoes/', AvaliacoesAPIView.as_view(), name='avaliacoes'),
    path('avaliacoes/<int:avaliacao_pk>/', AvaliacaoAPIView.as_view(), name='avaliacao')
]
"""