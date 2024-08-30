from django.urls import path
from rest_framework.routers import SimpleRouter
from .views import (
AvaliacaoApiView,
CursoApiView, 
AvaliacoesApiView, 
CursosApiView, 
ProfessorApiView,
CursoViewSet,
AvaliacaoViewSet,
ProfessorViewSet,
IndexView
)

router = SimpleRouter()
router.register('curso', CursoViewSet)
router.register('avaliacao', AvaliacaoViewSet)
router.register('professor', ProfessorViewSet)

urlpatterns = [
    path('', IndexView.as_view(), name='index'),
    path('cursos/', CursosApiView.as_view(), name='cursos'),
    path('cursos/<int:pk>/', CursoApiView.as_view(), name='curso'),
    path('cursos/<int:curso_id>/avaliacoes/', AvaliacaoApiView.as_view(), name='curso'),
    path('avaliacoes/', AvaliacoesApiView.as_view(), name='avaliacoes'),
    path('avaliacoes/<int:curso_id>/', AvaliacaoApiView.as_view(), name='avaliacao-curso'),
    path('professores/', ProfessorApiView.as_view(), name='professores')
   # V2
]