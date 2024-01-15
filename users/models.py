from django.db import models

class User(models.Model):
  name = models.CharField(max_length=255)
  email = models.EmailField()
  password = models.CharField(max_length=255)
  contato = models.CharField(max_length=255)
  empresa = models.CharField(max_length=255)
  contato_empresa = models.CharField(max_length=255)
  image = models.ImageField(upload_to='images/', null=True, blank=True)
  
  def __str__(self):
    return self.name
  
                            