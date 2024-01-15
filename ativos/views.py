from rest_framework import viewsets
from ativos.models import Arcondicionado
from .serializers import ArcondicionadoSerializer
from rest_framework.authentication import BasicAuthentication
from rest_framework.permissions import IsAuthenticated

class ArcondicionadoViewSet(viewsets.ModelViewSet):
  queryset = Arcondicionado.objects.all()
  serializer_class = ArcondicionadoSerializer
  authentication_classes = [BasicAuthentication]
  permission_classes = [IsAuthenticated]
  
  def perform_create(self, serializer):
        # Sobrescreva o método perform_create para lidar com o envio de arquivos
        documentos = self.request.data.getlist('documentos')
        imagens = self.request.data.getlist('imagens')

        # Se você precisar associar os arquivos ao objeto antes de salvar, faça aqui

        serializer.save()

  def perform_update(self, serializer):
      # Sobrescreva o método perform_update se necessário
      # para lidar com o envio de arquivos durante uma atualização
      documentos = self.request.data.getlist('documentos')
      imagens = self.request.data.getlist('imagens')

      # Lógica para processar arquivos durante a atualização

      serializer.save()

  def create(self, request, *args, **kwargs):
      # Sobrescreva o método create para lidar com a resposta após a criação
      response = super().create(request, *args, **kwargs)
      # Lógica adicional se necessário
      return response

  def update(self, request, *args, **kwargs):
      # Sobrescreva o método update se necessário
      response = super().update(request, *args, **kwargs)
      # Lógica adicional se necessário
      return response