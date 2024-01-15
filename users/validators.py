import re

def contato_valido(numero_do_contato):
  modelo = '[0-9]{2} [0-9]{5}-[0-9]{4}'
  resposta = re.findall(modelo, numero_do_contato)
  return resposta

def contato_empresa_valido(numero_da_empresa):
  modelo = '[0-9]{2} [0-9]{5}-[0-9]{4}'
  resposta = re.findall(modelo, numero_da_empresa)
  return resposta