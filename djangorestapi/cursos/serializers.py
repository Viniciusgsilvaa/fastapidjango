from rest_framework import serializers
from .models import Curso, Avaliacao, Professor

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

class ProfessorSerializer(serializers.ModelSerializer):
    curso = serializers.CharField(source='curso.titulo', read_only=True)

    class Meta:
        model = Professor
        fields = (
            'nome',
            'registro',
            'curso',
            'publicacao',
            'ativo'
        )

class CursoSerializer(serializers.ModelSerializer):
    professores = ProfessorSerializer(many=True, read_only=True)
    

    class Meta:
        model = Curso
        fields = (
            'id',
            'titulo',
            'url',
            'professores',
            'publicacao',
            'ativo'
        )



        