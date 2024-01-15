from ativos.models import Arcondicionado
from rest_framework import serializers
  
class ArcondicionadoSerializer(serializers.ModelSerializer):
  class Meta:
    model = Arcondicionado
    fields = '__all__'