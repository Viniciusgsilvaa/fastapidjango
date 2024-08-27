from rest_framework import serializers
from .models import Curso, Avaliacao

class AvaliacaoSerializer(serializers.ModelSerializer):
    curso = serializers.CharField(source='curso.titulo', read_only=True)

    class Meta:
        extra_kwargs = {
            'email': {'write_only': True}
        }
        model = Avaliacao
        fields = (
            'id',
            'curso',
            'email',
            'comentario',
            'avaliacao',
            'publicacao',
            'ativo'
        )


class CursoSerializer(serializers.ModelSerializer):

    class Meta:
        model = Curso
        fields = (
            'id',
            'titulo',
            'url',
            'publicacao',
            'ativo'
        )    
        