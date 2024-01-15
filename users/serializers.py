from users.models import User
from rest_framework import serializers
from users.validators import *

class UserSerializer(serializers.ModelSerializer):
  class Meta:
    model = User
    fields = '__all__'
    
  def validate(self, data):
    if not contato_valido(data['contato']):
      raise serializers.ValidationError({'contato':'Contato inválido'})
    if not contato_empresa_valido(data['contato_empresa']):
      raise serializers.ValidationError({'contato_empresa':'Contato inválido'})
    return data