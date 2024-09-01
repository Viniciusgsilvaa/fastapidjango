from rest_framework import generics
from .models import Curso, Avaliacao, Professor
from .serializers import CursoSerializer, AvaliacaoSerializer, ProfessorSerializer
from rest_framework import viewsets
from rest_framework.decorators import action
from rest_framework.response import Response
from django.views.generic import TemplateView
from rest_framework import permissions
from .permissions import IsSuperUser

class IndexView(TemplateView):
    template_name = 'index.html'
    

class CursoApiView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Curso.objects.all()
    serializer_class = CursoSerializer


class CursosApiView(generics.ListCreateAPIView):
    queryset = Curso.objects.all()
    serializer_class = CursoSerializer
    

class AvaliacoesApiView(generics.ListCreateAPIView):
    queryset = Avaliacao.objects.all()
    serializer_class = AvaliacaoSerializer 


class AvaliacaoApiView(generics.ListAPIView):
    serializer_class = AvaliacaoSerializer

    def get_queryset(self):
        curso_id = self.kwargs['curso_id']
        return Avaliacao.objects.filter(curso_id=curso_id)


class ProfessorApiView(generics.ListAPIView):
    queryset = Professor.objects.all()
    serializer_class = ProfessorSerializer


"""
API V2
"""

class CursoViewSet(viewsets.ModelViewSet):
    permission_classes = (IsSuperUser, permissions.DjangoModelPermissions,)
    queryset = Curso.objects.all()
    serializer_class = CursoSerializer

    @action(detail=True, methods=['get'])
    def avaliacoes(self, request, pk=None):
        curso = self.get_object()
        serializer = AvaliacaoSerializer(curso.avaliacoes.all(), many=True)
        return Response(serializer.data)

    @action(detail=True, methods=['get'])
    def professor(self, request, pk=None):
        curso = self.get_object()
        serializer = ProfessorSerializer(curso.professores.all(), many=True)
        return Response(serializer.data)

class AvaliacaoViewSet(viewsets.ModelViewSet):
    queryset = Avaliacao.objects.all()
    serializer_class = AvaliacaoSerializer


class ProfessorViewSet(viewsets.ModelViewSet):
    queryset = Professor.objects.all()
    serializer_class = ProfessorSerializer