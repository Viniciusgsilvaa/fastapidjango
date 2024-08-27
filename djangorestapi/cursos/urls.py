from django.urls import path
from .views import AvaliacaoApiView, CursoApiView, AvaliacoesApiView, CursosApiView

urlpatterns = [
    path('cursos/', CursosApiView.as_view(), name='cursos'),
    path('avaliacoes/', AvaliacoesApiView.as_view(), name='avaliacoes'),
    path('avaliacoes/<int:curso_id>/', AvaliacaoApiView.as_view(), name='avaliacao-curso'),
    path('cursos/<int:pk>/', CursoApiView.as_view(), name='curso')
]