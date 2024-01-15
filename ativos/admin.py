from django.contrib import admin
from ativos.models import Arcondicionado

class Arcondicionados(admin.ModelAdmin):
  list_display = ('id', 'codigo', 'marca', 'modelo', 'categoria', 'status', 'tipo_equipamento')
  list_display_links = ('id', 'codigo')
  search_fields = ('id',)
  list_per_page = 20
  
admin.site.register(Arcondicionado, Arcondicionados) 