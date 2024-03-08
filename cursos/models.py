from django.db import models
from django.contrib.auth.models import User
from django.db.models.signals import post_save, post_delete
from django.dispatch import receiver

class Base(models.Model):
    criado = models.DateTimeField(auto_now_add=True)
    modificado = models.DateTimeField(auto_now=True)
    ativo = models.BooleanField(default=True)

    class Meta:
        abstract = True

class Curso(Base):
    titulo = models.CharField(max_length=255)
    url = models.URLField(unique=True)
    media_avaliacoes = models.DecimalField(max_digits=5, decimal_places=2, default=0.0)

    class Meta:
        verbose_name = "Curso"
        verbose_name_plural = "Cursos"
        ordering = ["id"]
    
    def __str__(self):
        return self.titulo

class Avaliacao(Base):
    curso = models.ForeignKey(Curso, related_name="avaliacoes", on_delete=models.CASCADE)
    user = models.ForeignKey(User, related_name="avaliacoes", on_delete=models.CASCADE)
    comentario = models.TextField(blank=True, default="")
    avaliacao = models.DecimalField(max_digits=2, decimal_places=1)

    class Meta:
        verbose_name = "Avaliação"
        verbose_name_plural = "Avaliações"
        unique_together = ["user", "curso"]
        ordering = ["id"]
    
    def __str__(self):
        return f"{self.user} avaliou o curso {self.curso} com nota {self.avaliacao}"

# signals
@receiver(post_save, sender=Avaliacao)
def atualizar_media_avaliacoes(sender, instance, **kwargs):
    curso = instance.curso
    media = curso.avaliacoes.aggregate(models.Avg('avaliacao'))['avaliacao__avg']
    if media is None:
        media = 0.0
    curso.media_avaliacoes = round(media, 2)
    curso.save()

@receiver(post_delete, sender=Avaliacao)
def atualizar_media_avaliacoes_exclusao(sender, instance, **kwargs):
    curso = instance.curso
    media = curso.avaliacoes.aggregate(models.Avg('avaliacao'))['avaliacao__avg']
    if media is None:
        media = 0.0
    curso.media_avaliacoes = round(media, 2)
    curso.save()