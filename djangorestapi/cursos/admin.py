from django.contrib import admin
from .models import Avaliacao, Curso, Professor


class AvaliacaoAdmin(admin.ModelAdmin):
    list_display = ['nome', 'curso', 'avaliacao']


class CursoAdimin(admin.ModelAdmin):
    list_display = ['title', 'url']

admin.site.register(Avaliacao, AvaliacaoAdmin)
admin.site.register(Curso)
admin.site.register(Professor)
