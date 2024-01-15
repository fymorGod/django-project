from django.db import models
from django.contrib.postgres.fields import ArrayField

class Ativos(models.Model):
  codigo = models.CharField(max_length=120, blank=False)
  marca = models.CharField(max_length=120)
  modelo = models.CharField(max_length=120)
  
  CATEGORIA = (
    ('RF','Refrigeração'),
    ('EL', 'Elétrica'),
    ('TL', 'Telemetria'),
    ('IR', 'Irradiação')
  )
  categoria = models.CharField(max_length=2, choices=CATEGORIA, blank=False, null=False)
  STATUS = (
    ('F', 'Funcionando'),
    ('S', 'StandyBy'),
    ('DF', 'Defeito'),
    ('M', 'Manutenção')
  )
  status = models.CharField(max_length=2, choices=STATUS, blank=False, null=False)
  TIPO_EQUIPAMENTO = (
    ('AR', 'Arcondicionado'),
    ('CB', 'Cabo')
  )
  tipo_equipamento = models.CharField(max_length=120, choices=TIPO_EQUIPAMENTO, blank=False, null=False)
  
  class Meta:
    abstract = True

class Arcondicionado(Ativos):
  potencia = models.IntegerField()
  tensao = models.IntegerField()
  documents = ArrayField(models.FileField(upload_to='arcondicionado/documentos', blank=True), blank=True, null=True)
  images = ArrayField(models.ImageField(upload_to='arcondicionado/images', blank=True), blank=True, null=True)
  
  def __str__(self):
    return self.codigo