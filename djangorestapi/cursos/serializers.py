from rest_framework import serializers
from .models import Curso, Avaliacao

class AvaliacaoSerializer(serializers.ModelSerializer):

    class Meta:
        extra_kwargs = {
            'email': {'white_only': True}
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
        fields = ('id',
            'titulo',
            'url',
            'publicacao',
            'ativo'
        )    
        