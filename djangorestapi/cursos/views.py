from rest_framework import generics
from .models import Curso, Avaliacao
from .serializers import CursoSerializer, AvaliacaoSerializer

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
